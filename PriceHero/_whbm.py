from requests import get
from selectorlib import Extractor

def _whbm(whbm_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: h1.product-name
        xpath: null
        type: Text
    price:
        css: 'p.product-price-wrapper span.product-price'
        xpath: null
        type: Text
    """)
    headers = {
        'authority': 'www.whitehouseblackmarket.com',
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
    website = get(whbm_url, headers=headers)
    productdata = extractor.extract(website.text)
    return productdata