from cardmarket_api import (
    get_orders,
    get_wants_list,
    get_stock
    )

import requests_mock


def test_get_orders_mocked(capfd):
    mock_response = {
        'order': [
            {'idOrder': 1, 'status': 'bought'},
            {'idOrder': 2, 'status': 'received'},
            {'idOrder': 3, 'status': 'sent'}
        ]
    }

    with requests_mock.Mocker() as mock:
        mock.get(
            'https://api.cardmarket.com/ws/v2.0/output.json/orders',
            json = mock_response,
            status_code = 200
        )

        get_orders()
        out, _ = capfd.readouterr()

        assert 'Numero ordini: 3' in out
        assert 'Ordine ID: 1' in out
        assert 'Ordine ID: 2' in out

def test_get_wants_list_mocked(capfd):
    mock_response = {
        'wantslist': [
            {'idWantslist': 101, 'name': 'Lista Charizard'},
            {'idWantslist': 102, 'name': 'Lista Trainer'},
        ]
    }

    with requests_mock.Mocker() as mock:
        mock.get('https://api.cardmarket.com/ws/v2.0/output.json/wantslist', json=mock_response, status_code=200)
        get_wants_list()
        out, _ = capfd.readouterr()
        assert 'ID: 101, Nome: Lista Charizard' in out
        assert 'ID: 102, Nome: Lista Trainer' in out

def test_get_stock_mocked(capfd):
    mock_response = {
        'article': [
            {'idArticle': 301, 'product': {'product_name': 'Pikachu'}},
            {'idArticle': 302, 'product': {'product_name': 'Blastoise'}},
        ]
    }

    with requests_mock.Mocker() as mock:
        mock.get('https://api.cardmarket.com/ws/v2.0/output.json/stock', json=mock_response, status_code=200)
        get_stock()
        out, _ = capfd.readouterr()
        assert 'ID: 301, Nome: Pikachu' in out
        assert 'ID: 302, Nome: Blastoise' in out