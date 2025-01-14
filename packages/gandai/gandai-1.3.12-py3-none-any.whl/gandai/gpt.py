import openai
import plotly.express as px

from gandai import models, query, secrets

openai.api_key = secrets.access_secret_version("OPENAI_KEY")


def ask_gpt(prompt: str, max_tokens: int = 60):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "text-curie-003" for a less expensive engine
        prompt=prompt,
        max_tokens=max_tokens,
    )

    return response.choices[0].text.strip()


def get_suggested_search_phrase(search: models.Search) -> str:
    targets = query.search_target_by_last_event_type(
        search_uid=search.uid, last_event_type="client_approve"
    )
    resp = ask_gpt(
        f"What search phrase would you use to search Google Maps to find companies that look like this: {targets['description'].tolist()}",
        max_tokens=60,
    )
    return resp


def get_top_zip_codes(area: str, top_n: int = 25) -> list:
    resp = ask_gpt(
        f"As a python array List[str], the top {top_n} zip codes in {area} are:",
        max_tokens=1000,
    )
    return eval(resp)


def summarize_search_by(targets):
    px.histogram(targets, x="employees", nbins=20, height=400, width=400).show()

    print(targets["ownership"].value_counts())

    GPT_PROMPT = f"""
    The top three geographic areas, based on the {[desc for desc in targets['description'].dropna().sample(20)]} are:
    """

    print(ask_gpt(prompt=GPT_PROMPT))

    GPT_PROMPT = f"""
    Give me the company type, products and services, and end markets {[desc for desc in targets['description'].dropna().sample(20)]} are:
    """

    print(ask_gpt(prompt=GPT_PROMPT, max_tokens=100))
