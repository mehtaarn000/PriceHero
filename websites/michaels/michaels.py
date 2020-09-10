from selectorlib import Extractor
from requests import get

extractor = Extractor.from_yaml_file('selectors.yml')

def michaels(michaels_url):
    headers = {
        'authority': 'www.michaels.com',
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

    website = get(michaels_url, headers=headers)
    productdata = extractor.extract(website.text)
    print(productdata)

michaels('https://www.michaels.com/magnetic-photo-frames-by-studio-decor/M20000540.html?dwvar_M20000540_size=4%22%20x%204%22')