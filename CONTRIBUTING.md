# Contributing to PriceHero in 9 steps

## Step 0
Fork the repository, and clone it to your local machine. Add the remote as your fork's git url.
## Step 1
Download the selectorlib Chrome extension, which can be found [here](https://chrome.google.com/webstore/detail/selectorlib/llgknofgmghejanicfcjdibnhpofaefd?hl=en).

## Step 2
Read the documentation for selectorlib found [here](https://selectorlib.com/getting-started.html).

## Step 3
On the website that you are trying to add, find a page with the product on it. For example, for [BestBuy](https://www.bestbuy.com/site/apple-10-9-inch-ipad-air-latest-model-4th-generation-with-wi-fi-64gb-sky-blue/5985620.p?skuId=5985620).

## Step 4
Using the selectorlib Chrome extension, grab the name and price of the product. Click the "Export Selector YML" button to get the nessecary YML data for the product.

## Step 5
Copy and paste the following code into a file (in the PriceHero directory) titled _{website name}.py. For example, `_bestbuy.py`.
```py
from requests import get
from selectorlib import Extractor

def _website(website_url):
    extractor = Extractor.from_yaml_string("""
    name:
        css: h1
        xpath: null
        type: Text
    price:
        css: 'strong.price span'
        xpath: null
        type: Text
    """)
    headers = {
        'authority': 'www.website.com',
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
    website = get(website_url, headers=headers)
    productdata = extractor.extract(website.text)
    return productdata
```

Replace the `from_yaml_string` argument with your YML data and replace any mention of `website` with the website's name. 

## Step 6
Now, in the __init__.py file, add the import. Copy and paste the following code at the bottom of the file:
```py
def website(website_url : str) -> dict:
    """Scrape product information from website
    
    Keyword arguments:
    website_url -- a product url from website.com
    """
    website_product = _website._website(website_url)
    return website_product
```

Replace any mention of `website` with the website that you added.

## Step 7
In the README.md file, add 1 to the total number of websites, and add the new website's name to the list. In the supported_websites.md file, Add the number of the website (the last website's number + 1), and then the website's URL. 

## Step 8
Push your changes to your fork and open a PR with your fork on my repository. Thanks for contributing!