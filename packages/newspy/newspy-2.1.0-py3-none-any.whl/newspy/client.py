import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from newspy import newsorg, rss
from newspy.shared.models import Source, Channel, Article

default_client_config = {}

channels = {
    Channel.NEWSORG: newsorg,
    Channel.RSS: rss,
}


def configure(newsorg_api_key: str | None = None) -> None:
    global default_client_config

    if newsorg_api_key is None:
        newsorg_api_key = os.getenv("NEWSORG_API_KEY")

    default_client_config = {
        "newsorg_api_key": newsorg_api_key,
    }


def get_sources() -> list[Source]:
    sources = []
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(channels[key].client.get_sources) for key in channels
        ]

        for future in as_completed(futures):
            sources.extend([r.to_source() for r in future.result()])

    return sources


def get_articles() -> list[Article]:
    articles = []
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(channels[key].client.get_articles) for key in channels
        ]

        for future in as_completed(futures):
            articles.extend([r.to_article() for r in future.result()])

    return articles
