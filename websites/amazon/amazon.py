from selectorlib import Extractor
import requests 

extractor = Extractor.from_yaml_file('selectors.yml')
extractor2 = Extractor.from_yaml_file('selectors2.yml')

def amazon2(amazon_url2):
    headers2 = {
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
    
    website2 = requests.get(amazon_url2, headers=headers2)
    productdata2 = extractor2.extract(website2.text)
    print(productdata2)

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
    if productdata['price'] == None or productdata['name'] == None:
        amazon2(amazon_url)
    if productdata['price'] == None and productdata['name'] == None:
        pass
    else:
        print(productdata)
    
    productdata = extractor.extract(website.text)
    print(productdata)
