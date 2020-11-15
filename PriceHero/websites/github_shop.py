from selectorlib import Extractor
from requests import get

def github_shop(github_shop_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: h1.product__header__title
        xpath: null
        type: Text
    price:
        css: 'div.product__header__price span'
        xpath: null
        type: Text
    """)

    website = get(github_shop_url)
    productdata = extractor.extract(website.text)
    return productdata