"""
Now we have a list of ledger id from private_ledger
"""

import time
import os
import requests

from gen_secret import get_kraken_signature

# Read Kraken API key and secret stored in environment variables
api_url = "https://api.kraken.com"
api_key = os.environ.get('API_KEY_KRAKEN', "3QAmqFlyX2UFZ/0U/28tIWFk8DYlbNQoJGZOhpdMbnb8b1d/HSMdwaGy")
api_sec = os.environ.get('API_SEC_KRAKEN', '''0+LmAhaY43un3pAxatkB5eSB+aF/QW13GrbWc7qx/lcAXdoHQ4iM+pSh7JUbmcu5l3
i12vmv6drlPmtUA2F/Qw==''')

# Attaches auth headers and returns results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

# Construct the request and print the result
resp = kraken_request('/0/private/TradesHistory', {
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

print(resp.json())
