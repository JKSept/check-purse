import shutil
import requests
from config import API_KEY
from tokenlist import TOKEN_LIST
from display import token_display


token_string = ""
for key in TOKEN_LIST:
    token_string = token_string + key + ","

    
url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=" + token_string +
    "&vs_currencies=usd&include_24hr_change=true"
    f"&x_cg_demo_api_key={API_KEY}"
)


response = requests.get(url)
data = response.json()


columns, lines = shutil.get_terminal_size(fallback=(80, 20))
title_string = "CHECK-PURSE"
print(title_string.center(columns, "═"))


full_pos = 0
for key in TOKEN_LIST:
    token_price = data[key]["usd"]
    daily_change = data[key]["usd_24h_change"]
    token_name = TOKEN_LIST[key]["name"]
    token_holdings = TOKEN_LIST[key]["balance"]
    token_pos = token_holdings * token_price
    full_pos += token_pos
    print(token_display(key, token_name, token_price, daily_change, token_holdings, token_pos))


full_pos_string = f"TOTAL BALANCE: ${full_pos:,.2f}"
print(full_pos_string.center(columns, "═"))















