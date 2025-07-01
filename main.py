
import os
import time
import requests

TG_TOKEN = os.getenv("BOT_TOKEN")
TG_CHAT_ID = os.getenv("CHAT_ID")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

ETH_ADDRESSES = [
    os.getenv('address_1', '').strip(),
    os.getenv('address_2', '').strip(),
    os.getenv('address_3', '').strip(),
    os.getenv('address_4', '').strip(),
    os.getenv('address_5', '').strip(),
    os.getenv('address_6', '').strip(),
    os.getenv('address_7', '').strip(),
    os.getenv('address_8', '').strip(),
    os.getenv('address_9', '').strip(),
    os.getenv('address_10', '').strip(),
]

def send_message(text):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = {"chat_id": TG_CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram ERROR:", e)

def get_latest_eth_tx(address):
    try:
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={ETHERSCAN_API_KEY}"
        res = requests.get(url).json()
        txs = res.get("result", [])
        for tx in txs:
            if tx["to"].lower() == address.lower():
                return tx
    except Exception as e:
        print("ETH API ERROR:", e)
    return None

def get_price(symbol="ETHUSDT"):
    try:
        r = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}").json()
        return float(r["price"])
    except:
        return 0

def main():
    last_seen = {}
    while True:
        eth_price = get_price()
        for eth in ETH_ADDRESSES:
            tx = get_latest_eth_tx(eth)
            if tx and tx["hash"] != last_seen.get(eth):
                value = int(tx["value"]) / 1e18
                usd = value * eth_price
                msg = f"🟢 *ETH 入金*\n👤 从: `{tx['from']}`\n👥 到: `{tx['to']}`\n💰 {value:.6f} ETH ≈ ${usd:,.2f}"
                send_message(msg)
                last_seen[eth] = tx["hash"]
        time.sleep(10)

if __name__ == "__main__":
    main()
