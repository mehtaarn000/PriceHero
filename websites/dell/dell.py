from selectorlib import Extractor
from requests import get

def dell(dell_url):
    extractor = Extractor.from_yaml_file('dell_selectors.yml')
    extractor2 = Extractor.from_yaml_file('dell_selectors2.yml')
    headers = {
        'authority': 'www.dell.com',
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

    website = get(dell_url, headers=headers)
    productdata = extractor.extract(website.text)

    if productdata['name'] == None or productdata['price'] == None:
        productdata2 = extractor2.extract(website.text)
        return productdata2
    else:
        return productdata
