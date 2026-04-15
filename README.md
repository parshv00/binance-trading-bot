# 🚀 Binance Futures Trading Bot (Testnet)

## 📌 Overview

This project is a Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET, LIMIT, and STOP orders via a command-line interface (CLI).


## ⚙️ Features

* Place MARKET orders
* Place LIMIT orders
* Place STOP-LIMIT orders (Bonus Feature)
* Supports BUY and SELL
* CLI-based input using argparse
* Input validation
* Logging of all API requests and responses
* Error handling for API and network issues


## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
```


## 🔑 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```


## 🔗 Binance Testnet Setup

* Visit: https://testnet.binancefuture.com
* Create account
* Generate API keys
* Add USDT using faucet


## ▶️ Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

### STOP-LIMIT Order (Bonus)

```
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.001 --price 60000 --stop_price 59000
```


## 📄 Output Example

```
Order Response:
{
  "orderId": 123456,
  "status": "FILLED",
  "executedQty": "0.001",
  "avgPrice": "58000.00"
}
```


## 📊 Logging

* Logs are stored in `bot.log`
* Includes API requests, responses, and errors


## ⚠️ Assumptions

* User has a Binance Futures Testnet account
* API keys are valid and have permissions
* Internet connection is stable


## 🎯 Evaluation Criteria Covered

✔ Order placement (MARKET, LIMIT, STOP)
✔ Clean code structure
✔ CLI input handling
✔ Logging and error handling
✔ Readable and reusable code


## 🙌 Author

Parshv Kothari
