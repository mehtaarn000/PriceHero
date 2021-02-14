from requests import get
from selectorlib import Extractor

def _walmart(walmart_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: h1.prod-ProductTitle
        xpath: null
        type: Text
    dollars:
        css: 'section.prod-PriceSection span.hide-content span.price-characteristic'
        xpath: null
        type: Text
    cents:
        css: 'section.prod-PriceSection span.hide-content span.price-mantissa'
        xpath: null
        type: Text
    originaldollars:
        css: 'section.prod-PriceSection div.price-old span.price-characteristic'
        xpath: null
        type: Text
    originalcents:
        css: 'section.prod-PriceSection div.price-old span.price-mantissa'
        xpath: null
        type: Text
    """)
    headers = {
        'authority': 'www.walmart.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

    website = get(walmart_url, headers=headers)
    originalproductdata = extractor.extract(website.text)
    price = str(originalproductdata["dollars"]) + "." + str(originalproductdata["cents"])

    if originalproductdata["originaldollars"] == None and originalproductdata["originalcents"] == None:
        productdata = {"name": originalproductdata["name"], "price": price, "originalprice": None}
        return productdata
    else:
        originalprice = str(originalproductdata["originaldollars"]) + str(originalproductdata["originalcents"])
        productdata = {"name": originalproductdata["name"], "price": price, "originalprice": originalprice}
        return productdata