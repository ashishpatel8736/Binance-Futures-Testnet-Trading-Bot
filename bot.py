from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from logger import setup_logger

# Define missing constants for advanced order types
ORDER_TYPE_STOP_MARKET = 'STOP_MARKET'
ORDER_TYPE_STOP = 'STOP'
ORDER_TYPE_OCO = 'OCO'

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = setup_logger()
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            self.logger.info("Initialized Binance Futures Testnet client.")
        except Exception as e:
            print("Error initializing client:", e)
            self.logger.error(f"Error initializing client: {e}")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None, stop_limit_price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            if order_type == ORDER_TYPE_LIMIT:
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            if order_type == ORDER_TYPE_STOP_MARKET:
                params['stopPrice'] = stop_price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            if order_type == ORDER_TYPE_STOP:  # Stop-Limit
                params['stopPrice'] = stop_price
                params['price'] = stop_limit_price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            self.logger.info("Placing order: {}".format(params))
            order = self.client.futures_create_order(**params)
            self.logger.info("Order response: {}".format(order))
            return order
        except BinanceAPIException as e:
            print("Binance API Exception:", e)
            self.logger.error(f"Binance API Exception: {e}")
            return None
        except Exception as e:
            print("General Exception:", e)
            self.logger.error(f"General Exception: {e}")
            return None
