from flask import Flask, render_template_string, request
from bot import BasicBot

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Binance Testnet Trading Bot</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        form { max-width: 400px; margin: auto; }
        label { display: block; margin-top: 10px; }
        input, select { width: 100%; padding: 8px; margin-top: 4px; }
        button { margin-top: 20px; padding: 10px 20px; }
        .result { margin-top: 30px; padding: 15px; border: 1px solid #ccc; background: #f9f9f9; }
    </style>
</head>
<body>
    <h2>Binance Futures Testnet Trading Bot</h2>
    <form method="post">
        <label>API Key <input name="api_key" required></label>
        <label>API Secret <input name="api_secret" required></label>
        <label>Currency Type
            <select name="symbol" id="symbol_select" onchange="toggleSymbolInput()">
                <option value="BTCUSDT">BTCUSDT</option>
                <option value="ETHUSDT">ETHUSDT</option>
                <option value="BNBUSDT">BNBUSDT</option>
                <option value="SOLUSDT">SOLUSDT</option>
                <option value="XRPUSDT">XRPUSDT</option>
                <option value="ADAUSDT">ADAUSDT</option>
                <option value="DOGEUSDT">DOGEUSDT</option>
                <option value="MATICUSDT">MATICUSDT</option>
                <option value="LTCUSDT">LTCUSDT</option>
                <option value="OTHER">Other</option>
            </select>
        </label>
        <label id="custom_symbol_label" style="display:none;">Custom Symbol <input name="custom_symbol" id="custom_symbol_input"></label>
        <label>Side
            <select name="side">
                <option>BUY</option>
                <option>SELL</option>
            </select>
        </label>
        <label>Order Type
            <select name="order_type" id="order_type" onchange="toggleFields()">
                <option value="MARKET">MARKET</option>
                <option value="LIMIT">LIMIT</option>
                <option value="STOP">STOP</option>
            </select>
        </label>
        <label>Quantity <input name="quantity" type="number" step="any" required></label>
        <label id="price_label" style="display:none;">Price <input name="price" type="number" step="any"></label>
        <label id="stop_price_label" style="display:none;">Stop Price <input name="stop_price" type="number" step="any"></label>
        <button type="submit">Place Order</button>
    </form>
    <script>
        function toggleFields() {
            var type = document.getElementById('order_type').value;
            document.getElementById('price_label').style.display = (type === 'LIMIT' || type === 'STOP') ? '' : 'none';
            document.getElementById('stop_price_label').style.display = (type === 'STOP') ? '' : 'none';
        }
        function toggleSymbolInput() {
            var symbol = document.getElementById('symbol_select').value;
            var customLabel = document.getElementById('custom_symbol_label');
            var customInput = document.getElementById('custom_symbol_input');
            if (symbol === 'OTHER') {
                customLabel.style.display = '';
                customInput.required = true;
            } else {
                customLabel.style.display = 'none';
                customInput.required = false;
            }
        }
        window.onload = function() { toggleFields(); toggleSymbolInput(); };
    </script>
    {% if result %}
    <div class="result">
        <strong>{{ result['msg'] }}</strong><br>
        {% if result['order'] %}
        Order ID: {{ result['order'].get('orderId') }}<br>
        Status: {{ result['order'].get('status') }}<br>
        Details: <pre>{{ result['order'] }}</pre>
        {% endif %}
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        api_key = request.form['api_key'].strip()
        api_secret = request.form['api_secret'].strip()
        symbol = request.form['symbol']
        if symbol == 'OTHER':
            symbol = request.form['custom_symbol'].strip().upper()
        else:
            symbol = symbol.strip().upper()
        side = request.form['side'].upper()
        order_type = request.form['order_type'].upper()
        try:
            quantity = float(request.form['quantity'])
        except:
            quantity = 1
        price = request.form.get('price')
        stop_price = request.form.get('stop_price')
        price = float(price) if price else None
        stop_price = float(stop_price) if stop_price else None
        stop_limit_price = None
        if order_type == 'STOP':
            try:
                stop_limit_price = float(request.form.get('stop_limit_price', ''))
            except:
                stop_limit_price = None
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
            result = {'msg': 'Order placed successfully!', 'order': order}
        else:
            result = {'msg': 'Order failed. Check logs for details.', 'order': None}
    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(debug=True)
