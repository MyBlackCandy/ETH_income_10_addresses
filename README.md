# ETH Income Bot

This bot checks the latest ETH deposit transactions for up to 10 Ethereum addresses and sends a message via Telegram if a new incoming transaction is detected.

## Deployment

1. Set the following environment variables:
   - `BOT_TOKEN` – your Telegram bot token
   - `CHAT_ID` – your group or user chat ID
   - `ETHERSCAN_API_KEY` – your Etherscan API key

2. Deploy to [Railway](https://railway.app) or any Python environment that supports background services.

## Install

```
pip install -r requirements.txt
python main.py
```
