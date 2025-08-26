from API.utils.settings import BASE_URL
from time import sleep
import requests

RETRIES = 3

def api_request(method, path, **kwargs):
    url = f"{BASE_URL}{path}"

    for i in range(RETRIES):
        r = requests.request(method, url, timeout=5, **kwargs)
        if r.status_code < 500 or 1 == RETRIES-1:
            return r

        sleep(1 << i)