from .client import api_get

import urllib.parse


def search_products(product_name):
    base_url = 'https://api.cardmarket.com/ws/v2.0/output.json/products/find'
    full_url = f'{base_url}?search={urllib.parse.quote(product_name)}'
    response = api_get(full_url)
    print(response.text)

def get_product_details(product_id):
    url = f'https://api.cardmarket.com/ws/v2.0/output.json/products/{product_id}'
    response = api_get(url)
    print(response.text)