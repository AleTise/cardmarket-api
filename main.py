import requests
import urllib.parse
from oauth_utils import (
    generate_nonce,
    generate_timestamp,
    build_signature_base_string,
    signature_request
)

#Inserire qui le credenziali non appena fornite da Cardmarket
CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
ACCESS_TOKEN = 'access_token'
TOKEN_SECRET = 'token_secret'

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

if __name__ == '__main__':
    get_user_info('nobueno11')