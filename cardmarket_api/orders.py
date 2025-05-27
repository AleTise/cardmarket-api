from .client import api_get

def get_orders():
    url = 'https://api.cardmarket.com/ws/v2.0/output.json/orders'
    response = api_get(url)

    try:
        data = response.json()
        orders = data.get('order', [])
        print(f'Numero ordini: {len(orders)}')
        for order in orders[:3]:
            print(f"Ordine ID: {order.get('idOrder')}, Stato: {order.get('state')}")
    except Exception as e:
        print('Errore parsing JSON:', e)
        print('Risposta raw:', response.text)