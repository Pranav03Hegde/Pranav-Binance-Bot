import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
BASE_URL = os.getenv('BASE_URL')

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL

def validate_symbol(symbol):
    valid = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    if symbol not in valid:
        raise ValueError(f"Invalid symbol: {symbol}")
    return True

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return True

def validate_price(price):
    if price <= 0:
        raise ValueError("Price must be positive.")
    return True
