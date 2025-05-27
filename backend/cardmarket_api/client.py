from .auth import build_oauth_header

import requests


def api_get(url):
    headers = build_oauth_header('GET', url)
    response = requests.get(url, headers= headers)
    print(f'Status code: {response.status_code}')
    return response