"""
    Sumary:
    method: post
    headers requests:
    - API-Key
    - API-Sign: get_kraken_signature()
    - start
    - end
    response:
    - output_1.json
"""

import time
import os
import requests

from gen_secret import get_kraken_signature, kraken_request

def gettrade_by_ledgers(api_key, api_sec):
    # Construct the request and print the result
    resp = kraken_request('/0/private/Ledgers', {
        "nonce": str(int(1000*time.time())),
        "asset": "GBP",
        "type": "deposit"
        # "start": 1610124514,
        # "end": 1610124514 + 3*3600
    }, api_key, api_sec)
    #TODO:  get all pages here if they have more than 50 transactions
    return resp.json()
if __name__ == "__main__":
    api_key = os.environ.get('API_KEY_KRAKEN', "3QAmqFlyX2UFZ/0U/28tIWFk8DYlbNQoJGZOhpdMbnb8b1d/HSMdwaGy")
    api_sec = os.environ.get('API_SEC_KRAKEN', '''0+LmAhaY43un3pAxatkB5eSB+aF/QW13GrbWc7qx/lcAXdoHQ4iM+pSh7JUbmcu5l3
i12vmv6drlPmtUA2F/Qw==''')
    print(gettrade_by_ledgers(
        api_key, api_sec
    ))