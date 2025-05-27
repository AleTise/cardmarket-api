from dotenv import load_dotenv
from oauth_utils import (
    generate_nonce,
    generate_timestamp,
    build_signature_base_string,
    signature_request
)

import requests
import urllib.parse
import os


load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TOKEN_SECRET')

def get_user_info(username):
    method = 'GET'
    base_url = f'https://api.cardmarket.com/ws/v2.0/output.json/users/{username}'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)
    
    print(f'Status code: {response.status_code}')
    print(response.text)

def search_products(product_name):
    method = 'GET'
    base_url = 'https://api.cardmarket.com/ws/v2.0/output.json/products/find'

    full_url = f'{base_url}?search={urllib.parse.quote(product_name)}'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join(f'{k}="{urllib.parse.quote(str(v))}"'for k, v in oauth_params.items())
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(full_url, headers= headers)

    print(f"Status code: {response.status_code}")
    print(response.text)

def get_product_details(product_id):
    method = 'GET'
    base_url = f'https://api.cardmarket.com/ws/v2.0/output.json/products/{product_id}'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)

    print(f'Status code: {response.status_code}')
    print(response.text)

def get_sell_offers(product_id):
    method = 'GET'
    base_url = f'https://api.cardmarket.com/ws/v2.0/output.json/articles/{product_id}'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)

    print(f'Status code: {response.status_code}')
    print(response.text)

def get_orders():
    method = 'GET'
    base_url = 'https://api.cardmarket.com/ws/v2.0/output.json/orders'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)

    print(f'Status code: {response.status_code}')

    try:
        data = response.json()
        orders = data.get('order', [])
        print(f'Numero ordini: {len(orders)}')

        for order in orders[: 3]:
            id_ordine = order.get('idOrder')
            status = order.get('state') or order.get('status')
            print(f'Ordine ID: {id_ordine}, Stato: {status}')

    except Exception as e:
        print('Errore nel parsing JSON:', e)
        print('Risposta raw:', response.text)

def get_wants_list():
    method = 'GET'
    base_url = 'https://api.cardmarket.com/ws/v2.0/output.json/wantslist'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)

    print(f'Status code: {response.status_code}')

    try:
        data = response.json()
        
        for wl in data.get('wantslist', [])[: 3]:
            print(f"ID: {wl.get('idWantslist')}, Nome: {wl.get('name')}")
    except Exception as e:
        print('Errore parsing wantslist:', e)
        print('Risposta raw:', response.text)
        print("Risposta completa:", response.text)

def get_stock():
    method = 'GET'
    base_url = 'https://api.cardmarket.com/ws/v2.0/output.json/stock'

    oauth_params = {
        'oauth_consumer_key': CONSUMER_KEY,
        'oauth_token': ACCESS_TOKEN,
        'oauth_nonce': generate_nonce(),
        'oauth_timestamp': generate_timestamp(),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_version': '1.0'
    }

    base_string = build_signature_base_string(method, base_url, oauth_params)
    signature = signature_request(base_string, CONSUMER_SECRET, TOKEN_SECRET)
    oauth_params['oauth_signature'] = signature

    auth_header = 'OAuth ' + ', '.join([f'{k}="{urllib.parse.quote(str(v))}"' for k, v in oauth_params.items()])

    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }

    response = requests.get(base_url, headers= headers)

    print(f'Status code: {response.status_code}')

    try:
        data = response.json()
        
        for item in data.get('article', [])[: 3]:
            print(f"ID: {item.get('idArticle')}, Nome: {item.get('product', {}).get('product_name')}")
    except Exception as e:
        print('Errore parsing stock:', e)
        print('Risposta raw:', response.text)