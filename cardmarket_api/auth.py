from utils.oauth_utils import (
    generate_nonce,
    generate_timestamp,
    build_signature_base_string,
    signature_request
)

from .config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    TOKEN_SECRET
)

import urllib.parse


def build_oauth_header(method, base_url):
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

    return {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }