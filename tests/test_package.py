import os
import pytest
from pprint import pprint
from dotenv import load_dotenv
from keyvox.keyvox import KeyVox

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

kv = KeyVox(api_key=api_key, base_url=base_url)


@pytest.mark.skip
def test_articles_list():
    articles = kv.articles.list({
        'page': 2
    })
    pprint(articles)


@pytest.mark.skip
def test_articles_retrieve():
    article = kv.articles.retrieve(os.getenv('ARTICLE_ID'))
    pprint(article)


@pytest.mark.skip
def test_tags_list():
    tags = kv.tags.list()
    pprint(tags)


def test_tags_retrieve():
    tag = kv.tags.retrieve(os.getenv('TAG_ID'))
    pprint(tag)