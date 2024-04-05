import requets
"""
We start with example in output 2. Assume they buy this asset with the vol and sell with thid vol too

step 1: get price from coinmarketcap and assume we sell $BTC/USD at this time
step2: cacl gain and loss
"""
headers - {
    "X-CMC_PRO_API_KEY": "abcd"
}
price = requets.get("https://pro-api.coinmarketcap.com/v2/cryptocurrency/price-performance-stats/latest").json()

sample = {
    "TTTZW7-7IT3A-RPWMX3": 
    {
            "ordertxid": "OB6K5J-5GSFW-POPO3O",
            "postxid": "TKH2SE-M7IF5-CFI7LT",
            "pair": "XXBTZGBP",
            "time": 1709855519.91286,
            "type": "buy",
            "ordertype": "limit",
            "price": "52280.00000",
            "cost": "2071.56625",
            "fee": "3.31451",
            "vol": "0.03962445",
            "margin": "0.00000",
            "leverage": "0",
            "misc": "",
            "trade_id": 3609102,
            "maker": true
        }
}

transactionId = sample[samples.keys()[0]]["postxid"]
asset = "BTC"
transactionType = "sell"
salePrice = price # assume
costBasis = sample[samples.keys()[0]]["cost"] + sample[samples.keys()[0]]["fee"]
marketRate = price # asume we sell at the top
gainLoss = salePrice*sample[samples.keys()[0]]["vol"] - costBasis
totalPercentageChange = gainLoss/costBasis

output  = {
    "transactions": [
        {
        "transactionId": transactionId
        "asset": asset,
        "quantity": salePrice*sample[samples.keys()[0]]["vol"] ,
        "transactionType": transactionType,
        "costBasis": costBasis,
        "salePrice": salePrice,
        "marketRate": salePrice, # assume salePrice = marketPrice
        "gainLoss": totalGainLoss,
        "percentageChange": totalPercentageChange
        }
    ],
    "totalGainLoss": totalGainLoss,
    "totalPercentageChange": totalPercentageChange,
    "baseCurrency": "USD",
}