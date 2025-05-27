from cardmarket_api import (
    search_products,
    get_user_info,
    get_product_details,
    get_sell_offers,
    get_orders
    )

import argparse


def main():
    parser = argparse.ArgumentParser(description='Interfaccia CLI Cardmarket API')
    parser.add_argument('--user', help= 'Mostra info utente dato username')
    parser.add_argument('--search', help= 'Cerca prodotti per nome')
    parser.add_argument('--orders',action= 'store_true', help= 'Mostra ordini')
    parser.add_argument('--product', type= int, help= 'Dettagli prodotto per ID')
    parser.add_argument('--selloffers', type= int, help= 'Offerte vendita per ID prodotto')

    args = parser.parse_args()

    if args.user:
        get_user_info(args.user)
    elif args.search:
        search_products(args.search)
    elif args.orders:
        get_orders()
    elif args.product:
        get_product_details(args.product)
    elif args.selloffers:
        get_sell_offers(args.selloffers)
    else:
        parser.print_help()
    

if __name__ == '__main__':
    #get_user_info('nobueno11')
    #search_products('Charizard')
    #get_product_details(31123)
    #get_sell_offers(31123)
    #get_orders()
    main()