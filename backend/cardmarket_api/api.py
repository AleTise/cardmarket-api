from fastapi import FastAPI, Depends, Header, HTTPException, Request
from cardmarket_api import get_user_info, get_orders
from dotenv import load_dotenv

import os
import logging


app = FastAPI()
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chiave API finta per demo (es. da .env)
API_KEY = os.getenv("API_KEY")

async def check_api_key(request: Request, call_next):
    # Ignora le richieste preflight (OPTIONS)
    if request.method == "OPTIONS":
        return await call_next(request)

    x_api_key = request.headers.get("x-api-key")
    print(f"Received API key: {x_api_key}")

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return await call_next(request)

@app.get("/search")
async def search(product: str, api_key: str = Depends(check_api_key)):
    # qui entra solo se l'API key è valida
    return {"result": f"Risultati per {product}"}

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.url.path != "/open":  # bypass per eventuale route pubblica
        api_key = request.headers.get("X-API-Key")
        if api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Unauthorized")

    logger.info(f"Richiesta a {request.url.path}")
    return await call_next(request)

@app.get("/user")
def user(username: str):
    return get_user_info(username)

@app.get("/orders")
def orders():
    return get_orders()

async def check_api_key(x_api_key: str = Header(...)):
    print(f"Received API key: {x_api_key}")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")