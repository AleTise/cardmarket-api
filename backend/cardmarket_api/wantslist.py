from .client import api_get

def get_wants_list():
    url = 'https://api.cardmarket.com/ws/v2.0/output.json/wantslist'
    response = api_get(url)

    try:
        data = response.json()
        for wl in data.get('wantslist', [])[:3]:
            print(f"ID: {wl.get('idWantslist')}, Nome: {wl.get('name')}")
    except Exception as e:
        print('Errore parsing wantslist:', e)
        print('Risposta raw:', response.text)