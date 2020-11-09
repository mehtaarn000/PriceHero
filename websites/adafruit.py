from selectorlib import Extractor
from requests import get

def adafruit(adafruit_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: h1.products_name
        xpath: null
        type: Text
    price:
        css: 'div#prod-price span'
        xpath: null
        type: Text
    """)
    website = get(adafruit_url)
    productdata = extractor.extract(website.text)
    return productdata