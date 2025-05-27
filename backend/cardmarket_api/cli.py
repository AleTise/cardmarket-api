from cardmarket_api import (
    get_user_info,
    search_products,
    get_product_details,
    get_sell_offers,
    get_orders,
    get_wants_list,
    get_stock
)

from dotenv import load_dotenv

import click
import os


@click.command()
def setup():
    """Mostra le variabili d'ambiente caricate."""
    load_dotenv()
    print("Variabili d'ambiente caricate:")
    print(f"CONSUMER_KEY = {os.getenv('CONSUMER_KEY')}")
    print(f"CONSUMER_SECRET = {os.getenv('CONSUMER_SECRET')}")
    print(f"ACCESS_TOKEN = {os.getenv('ACCESS_TOKEN')}")
    print(f"TOKEN_SECRET = {os.getenv('TOKEN_SECRET')}")

@click.group()
def cli():
    """Cardmarket CLI Tool"""
    pass

@cli.command()
@click.argument('username')
def user(username):
    """"Mostra info utente"""
    get_user_info(username)

@cli.command()
@click.argument('query')
def search(query):
    """Cerca un prodotto"""
    search_products(query)

@cli.command()
def orders():
    """Mostra gli ordini"""
    get_orders()

@cli.command()
def wants():
    """Mostra wantslist"""
    get_wants_list()

@cli.command()
def stock():
    """Mostra lo stock"""
    get_stock()

@cli.command()
@click.argument('product_id', type=int)
def product(product_id):
    """Dettagli prodotto"""
    get_product_details(product_id)

@cli.command()
@click.argument('product_id', type=int)
def selloffers(product_id):
    """Offerte di vendita"""
    get_sell_offers(product_id)

cli.add_command(setup)

if __name__ == '__main__':
    cli()