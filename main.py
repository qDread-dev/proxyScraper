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

# Adds params to link
for key in proxyParams.keys():
    url = url.upper().replace(key, proxyParams[key])
url = url.lower()

#Grabs proxies

response = requests.request("GET", url, headers=headers, data=payload,timeout=5)
print(response.text)

proxyList = response.text.split("\n")
print(f"{len(proxyList)} Proxies scraped!")