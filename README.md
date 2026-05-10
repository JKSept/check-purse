# CHECK PURSE

A lightweight Python terminal application that tracks cryptocurrency holdings using live market data from the CoinGecko API.

CHECK PURSE displays your portfolio directly in the terminal using custom ASCII art, colored price indicators, 24-hour market changes, and calculated position values for each asset.

Designed as a simple and visually styled command-line dashboard for quickly checking crypto positions.

---

# Features

- Live cryptocurrency prices from CoinGecko
- 24-hour percentage change tracking
- Automatic position value calculations
- ANSI colored terminal output
- Custom ASCII art token displays
- Simple portfolio configuration
- Lightweight and dependency minimal

---

# Supported Assets

Currently configured assets:

- Bitcoin (BTC)
- Ethereum (ETH)
- XRP
- Chainlink (LINK)
- Hedera (HBAR)
- SPX6900
- Monad

Additional assets can be added using valid CoinGecko token IDs.

---

# Project Structure

```text
project/
├── main.py         # Main application logic
├── display.py      # ASCII art and formatted display functions
├── tokenlist.py    # User portfolio balances and token config
├── config.py       # CoinGecko API key
```

---

# Requirements

- Python 3.10+
- requests

Install dependencies:

```bash
pip install requests
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

---

## 2. Create a CoinGecko API Key

Create a free API key from:

https://www.coingecko.com/

---

## 3. Create `config.py`

Inside the project directory, create a file named:

```text
config.py
```

Add the following:

```python
API_KEY = "your_api_key_here"
```

---

# Configure Your Portfolio

Open `tokenlist.py` and edit your balances:

```python
# EDIT YOUR BALANCE HERE
link_balance = 100
xrp_balance = 1000
hbar_balance = 1000
spx_balance = 1000
monad_balance = 1000
eth_balance = 10
btc_balance = 1.5
```

You can also add new tokens to the `TOKEN_LIST` dictionary using valid CoinGecko IDs:

```python
TOKEN_LIST = {
    "bitcoin": {"name": "BTC", "balance": btc_balance},
    "ethereum": {"name": "ETH", "balance": eth_balance}
}
```

---

# Running the Application

Run the application from the terminal:

```bash
python main.py
```

---

# Example Output

The application displays:

- Token symbol
- Current market price
- 24-hour percentage change
- Holdings amount
- Total position value
- Custom ASCII artwork

All output is rendered directly inside the terminal.

---

# How It Works

1. `main.py` builds a CoinGecko API request using token IDs from `TOKEN_LIST`
2. Market data is fetched using the CoinGecko API
3. Position values are calculated based on balances
4. `display.py` formats the data into styled ASCII output
5. Portfolio information is printed to the terminal

---

# Notes

- Terminal must support ANSI escape colors for proper rendering
- Token IDs must match valid CoinGecko asset IDs
- API rate limits may apply depending on your CoinGecko plan

