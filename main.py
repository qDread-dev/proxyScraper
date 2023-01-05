import requests


url = "https://api.proxyscrape.com/v2/?request=proxyinfo"

headers={}
payload={}

response = requests.request("GET", url, headers=headers, data=payload,timeout=5)
print(response.text)