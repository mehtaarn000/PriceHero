from selectorlib import Extractor
import requests 
from time import sleep


# Create an Extractor by reading from the YAML file
extractor = Extractor.from_yaml_file('selectors.yml')

def amazon(amazon_url):    
    headers = {
        'authority': 'www.amazon.com',
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

    website = requests.get(amazon_url, headers=headers)

    productdata = extractor.extract(website.text)
    print(productdata)

#productdata = amazon('https://www.amazon.com/CanaKit-Raspberry-4GB-Starter-Kit/dp/B07V5JTMV9/ref=sr_1_1_sspa?crid=1L6CEL0UUWQRW&dchild=1&keywords=raspberry+pi+4&qid=1599443556&sprefix=rasp%2Caps%2C218&sr=8-1-spons&psc=1&smid=A30ZYR2W3VAJ0A&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMlJKNElMNDJOTDdCJmVuY3J5cHRlZElkPUEwOTYxMDI3NDVIMFFBMEFVR1dYJmVuY3J5cHRlZEFkSWQ9QTAxNTA5NzAzQlMxVTE3VFBZRzk2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')
#price = productdata['price']
#name = productdata['name']

amazon('https://www.amazon.com/CanaKit-Raspberry-4GB-Starter-Kit/dp/B07V5JTMV9/ref=sr_1_1_sspa?crid=1L6CEL0UUWQRW&dchild=1&keywords=raspberry+pi+4&qid=1599443556&sprefix=rasp%2Caps%2C218&sr=8-1-spons&psc=1&smid=A30ZYR2W3VAJ0A&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMlJKNElMNDJOTDdCJmVuY3J5cHRlZElkPUEwOTYxMDI3NDVIMFFBMEFVR1dYJmVuY3J5cHRlZEFkSWQ9QTAxNTA5NzAzQlMxVTE3VFBZRzk2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')
