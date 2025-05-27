from fastapi import FastAPI
from cardmarket_api import search_products


app = FastAPI()

@app.get("/search")
def search(query: str):
    return search_products(query)