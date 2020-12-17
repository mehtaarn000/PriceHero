from . import _amazon
from . import _bestbuy
from . import _dell
from . import _michaels
from . import _acer
from . import _walmart
from . import _adafruit
from . import _xbox
from . import _joanns
from . import _github_shop
from . import _macys

def a(self):
    amazon_product = _amazon(self)
    return amazon_product

def bestbuy(self):
    bestbuy_product = _bestbuy(self)
    return bestbuy_product

def dell(dell_url):
    dell_product = _dell(dell_url)
    return dell_product

def michaels(michaels_url):
    michaels_product = _michaels(michaels_url)
    return michaels_product

def acer(acer_url):
    acer_product = _acer(acer_url)
    return acer_product

def walmart(walmart_url):
    walmart_product = _walmart(walmart_url)
    return walmart_product

def adafruit(adafruit_url):
    adafruit_product = _adafruit(adafruit_url)
    return adafruit_product

def xbox(xbox_url):
    xbox_product = _xbox(xbox_url)
    return xbox_product

def joanns(joanns_url):
    joanns_product = _joanns(joanns_url)
    return joanns_product

def github_shop(github_shop_url):
    github_shop_product = _github_shop(github_shop_url)
    return github_shop_product

def macys(macys_url):
    macys_product = _macys(macys_url)
    return macys_product