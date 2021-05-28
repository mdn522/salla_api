import requests
import requests_cache
from rich import print
from .components.schemas import *


class SallaAPI:
    base_url = "https://api.salla.dev/admin/v2"

    def __init__(self, api_key):
        # self.session = requests_cache.CachedSession('amazon')
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": "Bearer {}".format(api_key)
        })
        pass

    def get_products(self, params=None):
        params = params or {}
        url = self.base_url + "/products"

        resp = self.session.get(url, params=params)

        # from core.utils.salla.generator.model import ProductsResponse
        # print(resp.json())
        return ProductsResponse(**resp.json())

    def product_details(self, product: int) -> Union[ProductResponse, NotFoundResponse]:
        url = self.base_url + f"/products/{product}"
        resp = self.session.get(url)
        resp_json = resp.json()

        if resp_json['status'] == 404:
            return NotFoundResponse(**resp_json)

        return ProductResponse(**resp_json)

    def product_details_by_sku(self, sku: str) -> Union[ProductResponse, NotFoundResponse]:
        url = self.base_url + f"/products/sku/{sku}"
        resp = self.session.get(url)
        resp_json = resp.json()

        if resp_json['status'] == 404:
            return NotFoundResponse(**resp_json)

        return ProductResponse(**resp_json)

    def update_product_price_by_sku(self, sku: str, price):
        url = self.base_url + f"/products/sku/{sku}/price"
        resp = self.session.post(url, data={'price': price})
        return resp.json()

    def list_product_variants(self, product: int) -> Union[ProductVariantsResponse, NotFoundResponse]:
        url = self.base_url + f"/products/{product}/variants"
        resp = self.session.get(url)
        resp_json = resp.json()

        if resp_json['status'] == 404:
            return NotFoundResponse(**resp_json)

        return ProductVariantsResponse(**resp_json)

    def get_product_variant(self, variant):
        url = self.base_url + f"/products/variants/{variant}"
        resp = self.session.get(url)
        return resp.json()

    def update_product_variant(self, variant, data):
        url = self.base_url + f"/products/variants/{variant}"
        resp = self.session.post(url, data=data)
        return resp.json()
