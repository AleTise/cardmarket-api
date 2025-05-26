import time
import random
import urllib.parse
import hmac
import hashlib
import base64

def generate_nonce(lenght= 8):
    return ''.join([str(random.randint(0, 9)) for _ in range(lenght)])

def generate_timestamp():
    return str(int(time.time()))

def percent_encode(s):
    return urllib.parse.quote(s, safe= '')

def build_signature_base_string(method, base_url, params):
    sorted_params = sorted(params.items())
    encode_params = urllib.parse.urlencode(sorted_params, quote_via= urllib.parse.quote)

    return '&'.join([
        method.upper(),
        percent_encode(base_url),
        percent_encode(encode_params)
    ])

def signature_request(base_string, consumer_secret, token_secret= ''):
    key = f'{percent_encode(consumer_secret)}&{percent_encode(token_secret)}'
    signature = hmac.new(
        key.encode('utf-8'),
        base_string.encode('utf-8'),
        hashlib.sha1
    ).digest()

    return base64.b64encode(signature).decode('utf-8')

