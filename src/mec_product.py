import json
import requests

from bs4 import BeautifulSoup


class MECProduct:
    _data: dict
    _offers: list[dict]
    _page: str
    _prices: list[float]
    _soup: BeautifulSoup
    _url: str

    name: str
    price: float

    def __init__(self, url: str):
        self._url = url
        self._page = self._get_page()
        self._soup = self._get_soup()
        self._data = self._get_data()
        self._offers = self._get_offers()
        self._prices = self._get_prices()
        self.name = self._get_name()
        self.price = self._get_price()

    def _get_page(self) -> str:
        return requests.get(self._url).text

    def _get_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self._page, 'lxml')

    def _get_data(self) -> dict[str, list]:
        scripts = self._soup.find('script', type='application/ld+json').string
        data: dict[str, list] = json.loads(scripts)
        return data

    def _get_name(self) -> str:
        return self._data['name']

    def _get_offers(self) -> list[dict]:
        offers: list[dict] = self._data['offers']
        return offers

    def _get_prices(self) -> list[float]:
        prices: list[float] = []
        for offer in self._offers:
            price = offer['price']
            prices.append(float(price))
        return prices

    def _get_price(self) -> float:
        return min(self._prices)
