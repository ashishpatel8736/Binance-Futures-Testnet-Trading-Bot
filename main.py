from binance.enums import *
from bot import BasicBot

def main():
    # Interactive input for all arguments
    api_key = input('Enter your Binance API Key: ').strip()
    api_secret = input('Enter your Binance API Secret: ').strip()
    
    # Currency (symbol) selection
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'MATICUSDT', 'LTCUSDT', 'Other']
    print('Select trading symbol:')
    for idx, sym in enumerate(symbols, 1):
        print(str(idx) + ". " + sym)
    while True:
        try:
            choice = int(input('Enter the number for your symbol: ').strip())
            if choice >= 1 and choice <= len(symbols):
                break
            else:
                print('Invalid selection. Try again.')
        except:
            print('Please enter a valid number.')
    if symbols[choice-1] == 'Other':
        symbol = input('Enter trading symbol (e.g., BTCUSDT): ').strip().upper()
    else:
        symbol = symbols[choice-1]
        
    side = input('Enter order side (BUY/SELL): ').strip().upper()
    while side not in ['BUY', 'SELL']:
        print('Invalid side. Please enter BUY or SELL.')
        side = input('Enter order side (BUY/SELL): ').strip().upper()
    order_type = input('Enter order type (MARKET/LIMIT/STOP): ').strip().upper()
    while order_type not in ['MARKET', 'LIMIT', 'STOP']:
        print('Invalid type. Please enter MARKET, LIMIT, or STOP.')
        order_type = input('Enter order type (MARKET/LIMIT/STOP): ').strip().upper()
    try:
        quantity = float(input('Enter order quantity: ').strip())
    except:
        print('Invalid quantity. Using 1.')
        quantity = 1
    price = None
    stop_price = None
    stop_limit_price = None
    if order_type in ['LIMIT', 'STOP']:
        try:
            price = float(input('Enter price: ').strip())
        except:
            print('Invalid price. Using 0.')
            price = 0
    if order_type == 'STOP':
        try:
            stop_price = float(input('Enter stop price: ').strip())
        except:
            print('Invalid stop price. Using 0.')
            stop_price = 0
        try:
            stop_limit_price = float(input('Enter stop-limit price: ').strip())
        except:
            print('Invalid stop-limit price. Using 0.')
            stop_limit_price = 0

    # Show order summary and confirm
    print("\nOrder Summary:")
    print("  Symbol:    " + str(symbol))
    print("  Side:      " + str(side))
    print("  Type:      " + str(order_type))
    print("  Quantity:  " + str(quantity))
    if price:
        print("  Price:     " + str(price))
    if stop_price:
        print("  StopPrice: " + str(stop_price))
    if stop_limit_price:
        print("  Stop-Limit Price: " + str(stop_limit_price))
    confirm = input("Proceed with this order? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Order cancelled by user.")
        return

    bot = BasicBot(api_key, api_secret)
    order = bot.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
        stop_price=stop_price,
        stop_limit_price=stop_limit_price
    )
    if order:
        print("\nOrder placed successfully!")
        print("Order ID: {}".format(order.get('orderId')))
        print("Status:   {}".format(order.get('status')))
        print("Details:  {}".format(order))
    else:
        print("Order failed. Check logs for details.")

if __name__ == "__main__":
    main()
