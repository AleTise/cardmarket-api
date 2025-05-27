from .client import api_get

def get_user_info(username):
    url = f'https://api.cardmarket.com/ws/v2.0/output.json/users/{username}'
    response = api_get(url)
    print(response.text)