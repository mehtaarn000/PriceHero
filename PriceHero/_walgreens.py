from requests import get
from selectorlib import Extractor

def _walgreens(walgreens_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: 'h1.product-name span.wag-text-black'
        xpath: null
        type: Text
    dollars:
        css: 'span.price__contain span.product__price span'
        xpath: null
        type: Text
    cents:
        css: 'span.price__contain sup:nth-of-type(2)'
        xpath: null
        type: Text
    """)
    headers = {
        'authority': 'www.walgreens.com',
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

    website = get(walgreens_url, headers=headers)
    productdata = extractor.extract(website.text)
    price = str(productdata["dollars"]) + "." + str(productdata["cents"])

    if productdata["dollars"] == None and productdata["cents"] == None:
        productdata["price"] = None

    else:
        del productdata["dollars"]
        del productdata["cents"]
        productdata["price"] = price

    return productdata