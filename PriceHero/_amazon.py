from requests import get
from selectorlib import Extractor

def _amazon(amazon_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: 'h1.a-spacing-none span.a-size-large'
        xpath: null
        type: Text
    price:
        css: 'div.a-section.a-spacing-micro span.a-size-medium'
        xpath: null
        type: Text
    """)   

    extractor2 = Extractor.from_yaml_string("""
    name:
        css: 'h1.a-size-large span.a-size-large'
        xpath: null
        type: Text
    price:
        css: 'div#priceInsideBuyBox_feature_div.celwidget span.a-size-medium'
        xpath: null
        type: Text
    """)

    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/50 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

    website = get(amazon_url, headers=headers)

    productdata = extractor.extract(website.text)
    if productdata["name"] == None or productdata["price"] == None:
        productdata2 = extractor2.extract(website.text)
        return productdata2
    else:
        return productdata
