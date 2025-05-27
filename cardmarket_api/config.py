from dotenv import load_dotenv

import os


load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TOKEN_SECRET')