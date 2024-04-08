"""
We start with example in output 2. Assume they buy this asset with the vol and sell with thid vol too

step 1: get price from coinmarketcap and assume we sell $BTC/USD at this time
step2: cacl gain and loss
"""
import os
import pandas as pd
from functools import reduce
import requests
from private_ledgers import gettrade_by_ledgers
from private_trade_history import get_trades_by_account

try:
    headers = {
        "X-CMC_PRO_API_KEY": "abcd"
    }
    price = requets.get("https://pro-api.coinmarketcap.com/v2/cryptocurrency/price-performance-stats/latest").json()
except:
    price = 100*10**3 #GDP

def calc_tax_by_asset():
    pass

def calc_all_gbp_deposit(api_key, api_sec):
    all_ledgers = gettrade_by_ledgers(
        api_key, api_sec
    )["result"]["ledger"]

    tatol_deposit_amount = reduce(lambda acc, key: acc + float(all_ledgers[key]["amount"]), all_ledgers, 0)
    print("tatol_deposit_amount: ", tatol_deposit_amount)
    return tatol_deposit_amount

def calc_gain_loss(api_key, api_sec):
    account_trades = get_trades_by_account(
        api_key, api_sec
    )["result"]["trades"]

    outputs = []
    for tx_id in account_trades.keys():
        transactionId = account_trades[tx_id]["ordertxid"]
        asset = account_trades[tx_id]["pair"]
        transaction_type = account_trades[tx_id]["type"]
        sale_price = price # asume we sell at the top of code
        cost_basis = float(account_trades[tx_id]["cost"]) + float(account_trades[tx_id]["fee"])
        market_rate = price # asume we sell at the top of code
        gain_loss = sale_price*float(account_trades[tx_id]["vol"]) - float(cost_basis)
        total_percentage_change = gain_loss/cost_basis

        output  = {
                    "transactionId": transactionId,
                    "asset": asset,
                    "quantity": float(sale_price)*float(account_trades[tx_id]["vol"]) ,
                    "transactionType": transaction_type,
                    "costBasis": cost_basis,
                    "salePrice": sale_price,
                    "marketRate": sale_price, # assume salePrice = marketPrice
                    "gainLoss": gain_loss,
                    "percentageChange": total_percentage_change
                }
        outputs.append(output)
    return outputs

def calc_total(api_key, api_sec):
    total_deposit = calc_all_gbp_deposit(
        api_key, api_sec
    )
    transactions = calc_gain_loss(
        api_key, api_sec
    )
    total_gain_loss = reduce(lambda acc, obj: acc + obj["gainLoss"], transactions, 0)
    outputs = {
        "transactions": transactions,
        "totalGainLoss": total_gain_loss,
        "totalPercentageChange": total_gain_loss/total_deposit,
        "baseCurrency": "GBP",
    }
    return outputs

if __name__ == "__main__":
    api_key = os.environ.get('API_KEY_KRAKEN', "3QAmqFlyX2UFZ/0U/28tIWFk8DYlbNQoJGZOhpdMbnb8b1d/HSMdwaGy")
    api_sec = os.environ.get('API_SEC_KRAKEN', '''0+LmAhaY43un3pAxatkB5eSB+aF/QW13GrbWc7qx/lcAXdoHQ4iM+pSh7JUbmcu5l3
        i12vmv6drlPmtUA2F/Qw=='''
    )
    print(calc_total(api_key, api_sec))