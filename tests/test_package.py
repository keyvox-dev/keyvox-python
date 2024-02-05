import os
import pytest
from pprint import pprint
from dotenv import load_dotenv
from keyvox.keyvox import KeyVox
import json

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


@pytest.mark.skip
def test_tags_retrieve():
    tag = kv.tags.retrieve(os.getenv('TAG_ID'))
    tag = json.dumps(tag, indent=4)
    pprint(tag)


@pytest.mark.skip
def test_authors_list():
    authors = kv.authors.list()
    authors = json.dumps(authors, indent=4)
    pprint(authors)


def test_authors_retrieve():
    author = kv.authors.retrieve(os.getenv('AUTHOR_ID'))
    author = json.dumps(author, indent=4)
    pprint(author)
