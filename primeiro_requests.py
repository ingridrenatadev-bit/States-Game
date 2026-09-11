import requests

respost = requests.get('https://hub.asimov.academy/')

print(respost.status_code)