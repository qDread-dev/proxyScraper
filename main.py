import requests

#edit for different settings, leave alone for default
proxyParams = {
    "PARAMREQ" : "displayproxies",
    "PARAMPROTOCOL" : "http",
    "PARAMTIMEOUT" : "10000",
    "PARAMCOUNTRY" : "all",
    "PARAMSSL" : "all",
    "PARAMANON" : "all"
}

url = "https://api.proxyscrape.com/v2/?request=PARAMREQ&protocol=PARAMPROTOCOL&timeout=PARAMTIMEOUT&country=PARAMCOUNTRY&ssl=PARAMSSL&anonymity=PARAMANON"

headers={}
payload={}

print(f"Before change {url}")
for key in proxyParams.keys():
    url = url.upper().replace(key, proxyParams[key])
url = url.lower()
print(f"After change {url}")
# response = requests.request("GET", url, headers=headers, data=payload,timeout=5)
# print(response.text)