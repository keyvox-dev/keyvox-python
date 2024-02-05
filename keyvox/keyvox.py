from requests import get, Response
from keyvox._article import Article
import urllib.parse

class KeyVox:
    def __init__(self, api_key: str, base_url: str = 'https://keyvox.dev/api'):
        self.api_key = api_key
        self.base_url = base_url
        self.articles = Article(self)

    def fetch_data(self, url: str, params: dict) -> Response:
        try:
            response = get(
                url=url,
                headers={
                    'key': self.api_key,
                    'lang': 'python'
                },
                params=params
            )

            return response.json()
        except Exception as error:
            print(error)
