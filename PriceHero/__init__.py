__version__ = "0.3.3"
__author__ = "mehtaarn000"

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
from . import _chess_shop
from . import _newegg

def amazon(amazon_url : str) -> dict:
    amazon_product = _amazon._amazon(amazon_url)
    return amazon_product

def bestbuy(bestbuy_url : str) -> dict:
    bestbuy_product = _bestbuy._bestbuy(bestbuy_url)
    return bestbuy_product

def dell(dell_url : str) -> dict:
    dell_product = _dell._dell(dell_url)
    return dell_product

def michaels(michaels_url : str) -> dict:
    michaels_product = _michaels._michaels(michaels_url)
    return michaels_product

def acer(acer_url : str) -> dict:
    acer_product = _acer._acer(acer_url)
    return acer_product

def walmart(walmart_url : str) -> dict:
    walmart_product = _walmart._walmart(walmart_url)
    return walmart_product

def adafruit(adafruit_url : str) -> dict:
    adafruit_product = _adafruit._adafruit(adafruit_url)
    return adafruit_product

def xbox(xbox_url : str) -> dict:
    xbox_product = _xbox._xbox(xbox_url)
    return xbox_product

def joanns(joanns_url : str) -> dict:
    joanns_product = _joanns._joanns(joanns_url)
    return joanns_product

def github_shop(github_shop_url : str) -> dict:
    github_shop_product = _github_shop._github_shop(github_shop_url)
    return github_shop_product

def macys(macys_url : str) -> dict:
    macys_product = _macys._macys(macys_url)
    return macys_product

def chess_shop(chess_shop_url : str) -> dict:
    chess_shop_product = _chess_shop._chess_shop(chess_shop_url)
    return chess_shop_product

def newegg(newegg_url : str) -> dict:
    newegg_product = _newegg._newegg(newegg_url)
    return newegg_product