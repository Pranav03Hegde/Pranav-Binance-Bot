from utils import client, validate_symbol, validate_quantity
from logger import setup_logger
import sys

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    try:
        validate_symbol(symbol)
        validate_quantity(quantity)
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Market Order: {side} {quantity} {symbol} - SUCCESS")
        print("✅ Market Order placed successfully!")
        return order
    except Exception as e:
        logger.error(f"Market Order Error: {str(e)}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL SIDE QUANTITY")
    else:
        _, symbol, side, quantity = sys.argv
        place_market_order(symbol, side.upper(), float(quantity))
