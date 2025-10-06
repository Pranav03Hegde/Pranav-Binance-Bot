from utils import client, validate_symbol, validate_quantity, validate_price
from logger import setup_logger
import sys

logger = setup_logger()

def place_limit_order(symbol, side, quantity, price):
    try:
        validate_symbol(symbol)
        validate_quantity(quantity)
        validate_price(price)
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        logger.info(f"Limit Order: {side} {quantity} {symbol} at {price} - SUCCESS")
        print("✅ Limit Order placed successfully!")
        return order
    except Exception as e:
        logger.error(f"Limit Order Error: {str(e)}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL SIDE QUANTITY PRICE")
    else:
        _, symbol, side, quantity, price = sys.argv
        place_limit_order(symbol, side.upper(), float(quantity), float(price))
