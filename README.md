# Binance Futures Testnet Trading Bot

## 🚀 Overview

A Python-based trading bot for the Binance USDT-M Futures Testnet. Place market, limit, and stop-limit orders with a user-friendly command-line interface and a lightweight web frontend. Designed for learning, testing, and rapid prototyping—**no real funds required!**

## ✨ Features

- **Interactive CLI** – Guided prompts for all order parameters (API key, symbol, side, type, quantity, price, etc.)
- **Web Frontend** – Simple Flask app for placing orders from your browser
- **Order Types** – Supports Market, Limit, and Stop-Limit orders (buy/sell)
- **Logging** – All API requests, responses, and errors are logged to `bot.log`
- **Input Validation** – Prevents invalid or incomplete orders
- **Reusable Code** – Modular `BasicBot` class for easy extension
- **Testnet Safe** – Uses only Binance Futures Testnet (no real money)

## 📂 Project Structure

```
bot2/
├── app.py            # Flask web frontend
├── main.py           # Command-line interface
├── bot.py            # Trading bot logic (BasicBot class)
├── logger.py         # Logging setup (console + file)
├── requirements.txt  # Python dependencies
├── bot.log           # Log file (auto-generated)
└── README.md         # Project documentation
```

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd bot2
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Get Binance Testnet API Keys

- Register at [https://testnet.binancefuture.com/](https://testnet.binancefuture.com/)
- Create API keys in the API Management section
- Enable Futures trading for the key

## 🚦 Usage

### ▶️ Command-Line Interface

```bash
python main.py
```
- Follow the prompts to enter your API key, symbol, order type, etc.
- Order status and details will be shown in the terminal.

### 🌐 Web Frontend

```bash
python app.py
```
- Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Fill in the form and submit orders from your browser.

## 📝 Order Types Supported

| Type        | Description                        |
|-------------|------------------------------------|
| MARKET      | Buy/sell at current market price   |
| LIMIT       | Buy/sell at a specific price       |
| STOP-LIMIT  | Trigger a limit order at a price   |

## 🛡️ Logging
- All actions and errors are logged to `bot.log` in the project folder.

## 👤 Author
**Ashish Patel**  
[![GitHub](logo\icons8-github-50.png)](https://github.com/ashishpatel8736) | [![LinkedIn](https://img.icons8.com/ios-filled/50/0077b5/linkedin.png)](https://www.linkedin.com/in/ashishpatel8736)

## 📜 License
MIT License. See `LICENSE` for details.

---

*For educational and testing use only. Not for real trading!*
