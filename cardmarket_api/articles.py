from .client import api_get

def get_sell_offers(product_id):
    url = f'https://api.cardmarket.com/ws/v2.0/output.json/articles/{product_id}'
    response = api_get(url)
    print(response.text)

def get_stock():
    url = 'https://api.cardmarket.com/ws/v2.0/output.json/stock'
    response = api_get(url)

    try:
        data = response.json()
        for item in data.get('article', [])[:3]:
            print(f"ID: {item.get('idArticle')}, Nome: {item.get('product', {}).get('product_name')}")
    except Exception as e:
        print('Errore parsing stock:', e)
        print('Risposta raw:', response.text)