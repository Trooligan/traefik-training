import requests
import time

url = "http://localhost/"
headers = {'Host': 'whoami.localhost'}

while True:
    r = requests.get(url, headers=headers)
print(r.status_code)



