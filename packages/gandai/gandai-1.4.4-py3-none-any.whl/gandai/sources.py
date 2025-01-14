import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List

import googlemaps
import pandas as pd
import requests

from gandai import gpt, helpers, models, query, secrets, constants


gmaps = googlemaps.Client(key=secrets.access_secret_version("GOOLE_MAPS_KEY"))
MAX_WORKERS = 25


class GoogleMapsWrapper:
    @staticmethod
    def get_loc(text: str = "San Diego, CA") -> tuple:
        resp = gmaps.geocode(text)
        return tuple(resp[0]["geometry"]["location"].values())

    @staticmethod
    def enrich(place_id: str) -> dict:
        resp = gmaps.place(place_id=place_id)
        return resp["result"]

    @staticmethod
    def fetch_unique_place_ids(
        search_phrase: str, locations: List[str], radius_miles: int = 25
    ) -> list:
        main_func = partial(
            GoogleMapsWrapper._fetch_place_ids,
            search_phrase=search_phrase,
            radius_miles=radius_miles,
        )
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exec:
            futures = exec.map(main_func, locations)

        place_ids = []
        for future in futures:
            try:
                place_ids.extend(list(future))
            except Exception as e:
                print(e)

        place_ids = list(set(place_ids))
        len(place_ids)
        return place_ids

    @staticmethod
    def _fetch_place_ids(
        location_text: str, search_phrase: str, radius_miles: int = 25
    ) -> list:
        try:
            METERS_PER_MILE = 1609.34
            radius_meters = radius_miles * METERS_PER_MILE

            loc: tuple = GoogleMapsWrapper.get_loc(location_text)

            results = []

            response = gmaps.places(
                query=search_phrase,
                location=loc,
                radius=radius_meters,
            )

            results.extend(response["results"])
            next_page_token = response.get("next_page_token", None)
            while next_page_token:
                time.sleep(2)
                response = gmaps.places(
                    query=search_phrase,
                    location=loc,
                    radius=radius_meters,
                    page_token=next_page_token,
                )
                results.extend(response["results"])
                next_page_token = response.get("next_page_token", None)

            place_ids = [result["place_id"] for result in results]
            print(
                f"{search_phrase} in {location_text} within {radius_miles} miles -> {len(place_ids)} results"
            )
            return place_ids
        except Exception as e:
            print(f"Error with {location_text} {search_phrase}: {e}")
            return []

    @staticmethod
    def build_target_from_place_id(
        place_id: str, search_uid: int, append_to_prompt: str = None
    ) -> models.Company:
        """takes in an (eriched) place and inserts it as a company"""
        # really more of an upsert, but multiple txns for now

        place = GoogleMapsWrapper.enrich(place_id)

        existing_search_domains = query.unique_domains(search_uid=search_uid)[
            "domain"
        ].to_list()

        if "website" not in place:
            print(f"no website for {place_id}")
            return

        # actually this should cache the result on the company....
        if helpers.clean_domain(place["website"]) in existing_search_domains:
            print(f"skipping {place['website']} - already in search_uid {search_uid}")
            return

        gpt_prompt = (" ").join(
            [
                f"Q: Based on these reviews:",
                f"{[review['text'] for review in place['reviews']]}",
                f"as well as what you already know about {place['website']},",
                f"what products and services does {place['name']} offer?",
            ]
        )
        if append_to_prompt:
            gpt_prompt += " " + append_to_prompt
        # print(gpt_prompt)

        company = models.Company(
            name=place["name"],
            domain=helpers.clean_domain(place["website"]),
            description="",
        )

        query.insert_company(company)  # on conflict does nothing

        # save the place in meta
        company = query.find_company_by_domain(company.domain)
        if "google_places" not in company.meta:
            company.meta["google_places"] = {}
        company.meta["google_places"][place_id] = place
        query.update_company(company)
        ###

        print(f"adding {company.domain} - search_uid {search_uid}")
        query.insert_event(
            models.Event(
                search_uid=search_uid,
                actor_key="chatgpt",
                type="comment",
                domain=company.domain,
                data={"comment": f"chatgpt - {gpt.ask_gpt(gpt_prompt)}"},
            )
        )

        query.insert_event(
            models.Event(
                search_uid=search_uid,
                actor_key="google",
                type="create",
                domain=company.domain,
            )
        )

        return company

    def build_place_ids_async(place_ids: list, search: models.Search):
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for place_id in place_ids:
                executor.submit(
                    GoogleMapsWrapper.build_target_from_place_id,
                    place_id=place_id,
                    search_uid=search.uid,
                )


class GrataWrapper:
    HEADERS = {
        "Authorization": secrets.access_secret_version("GRATA_API_TOKEN"),
        "Content-Type": "application/json",
    }

    def find_similar(domain: str, search: models.Search) -> list:
        api_filters = GrataWrapper._get_api_filter(search)
        similiar_filters = {
            "domain": domain,
            "grata_employees_estimates_range": api_filters[
                "grata_employees_estimates_range"
            ],
            "headquarters": api_filters["headquarters"],
            "ownership": api_filters["ownership"],
            "exclude": api_filters["exclude"],
        }
        # print(similiar_filters)
        response = requests.post(
            "https://search.grata.com/api/v1.2/search-similar/",
            headers=GrataWrapper.HEADERS,
            json=similiar_filters,
        )
        data = response.json()
        # print("find_similar:", data)
        data["companies"] = data.get("results", [])  # asking grata about this

        return data["companies"]


    def find_by_criteria(search: models.Search) -> list:
        pages = search.context.get('result_count', 25) / 25
        companies = []
        api_filters = GrataWrapper._get_api_filter(search)
        def _find_by_criteria(api_filters: dict, page_token=None) -> dict:
            if page_token:
                api_filters["page_token"] = page_token
            response = requests.post(
                "https://search.grata.com/api/v1.2/search/",
                headers=GrataWrapper.HEADERS,
                json=api_filters,
            )
            data = response.json()
            return data
        resp = _find_by_criteria(api_filters)
        page_token = resp.get("page_token")
        companies.extend(resp["companies"])
        if pages > 1:
            for _ in range(1, int(pages)):
                resp = _find_by_criteria(api_filters, page_token)
                companies.extend(resp["companies"])
                page_token = resp.get("page_token")
                if not page_token:
                    break
        return companies

    def enrich(domain: str) -> dict:
        response = requests.post(
            "https://search.grata.com/api/v1.2/enrich/",
            headers=GrataWrapper.HEADERS,
            json={"domain": domain},
        )
        data = response.json()
        data["linkedin"] = data.get("social_linkedin")
        data["ownership"] = data.get("ownership_status")
        return data

    def enrich_targets_async(targets: pd.DataFrame) -> None:
        def enrich_company_by_domain(domain: str) -> None:
            company = query.find_company_by_domain(domain)
            if "company_uid" not in company.meta.keys():
                # print(company.name)
                resp = GrataWrapper.enrich(domain)
                company.description = resp.get("description")
                company.meta = {**company.meta, **resp}  # merge 3.5+
                query.update_company(company)

            with ThreadPoolExecutor(max_workers=5) as executor:
                executor.map(enrich_company_by_domain, targets["domain"].tolist())

    def _get_api_filter(search: models.Search) -> dict:

        def _hq_include() -> list:
            hq_include = []
            cities = search.inclusion.get("city", [])
            states = search.inclusion.get("state", [])
            countries = search.inclusion.get("country", [])

            if len(cities) > 0:
                # front-end validates only one state when city selected
                state = constants.STATES[states[0]]
                for city in cities:
                    hq_include.append(
                        {"city": city, "state": state, "country": "United States"}
                    )
                return hq_include

            if len(states) > 0:
                for state in states:
                    hq_include.append({"state": constants.STATES[state]})
            elif len(countries) > 0:
                for country in countries:
                    hq_include.append({"country": constants.COUNTRIES[country]})
            return hq_include

        def _hq_exclude() -> list:
            hq_exclude = []
            for state in search.exclusion.get("state", []):
                hq_exclude.append({"state": constants.STATES[state]})
            return hq_exclude

        api_filters = {
            "op": search.context.get("operator", "all"),
            "include": search.inclusion.get("keywords", []),
            "exclude": search.exclusion.get("keywords", []),
            "grata_employees_estimates_range": search.inclusion.get("employees_range", []),
            "ownership": search.inclusion.get("ownership", ""),
            "headquarters": {
                "include": _hq_include(),
                "exclude": _hq_exclude(),
            },
        }
        # print(api_filters)
        return api_filters


class SourceScrubWrapper:
    def find_similar(domain: str, search: models.Search) -> dict:
        pass

    def find_by_criteria(search: models.Search) -> dict:
        pass

    def enrich(domain: str) -> dict:
        pass
