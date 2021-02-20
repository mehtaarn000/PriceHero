# -*- coding: utf-8 -*-

__version__ = "0.3.9"
__author__ = "mehtaarn000"
__license__ = "MIT"
__maintainer__ = "mehtaarn000"
__credits__ = ["mehtaarn000", "kilianalias", "nethracookie"]

"""A python module that will allow users to get product prices information from a multitude of different websites."""
from . import (
    _amazon,
    _bestbuy,
    _dell,
    _michaels,
    _acer,
    _walmart,
    _adafruit,
    _xbox,
    _joanns,
    _github_shop,
    _macys,
    _chess_shop,
    _newegg,
    _etsy,
    _overstock,
    _pishop,
    _boohoo
)

def amazon(amazon_url : str) -> dict:
    """Scrape product information from amazon.com
    
    Keyword arguments:
    amazon_url -- a product url from amazon.com
    """
    amazon_product = _amazon._amazon(amazon_url)
    return amazon_product

def bestbuy(bestbuy_url : str) -> dict:
    """Scrape product information from bestbuy.com
    
    Keyword arguments:
    bestbuy_url -- a product url from bestbuy.com
    """
    bestbuy_product = _bestbuy._bestbuy(bestbuy_url)
    return bestbuy_product

def dell(dell_url : str) -> dict:
    """Scrape product information from dell.com
    
    Keyword arguments:
    dell_url -- a product url from dell.com
    """
    dell_product = _dell._dell(dell_url)
    return dell_product

def michaels(michaels_url : str) -> dict:
    """Scrape product information from michaels.com
    
    Keyword arguments:
    michaels_url -- a product url from michaels.com
    """
    michaels_product = _michaels._michaels(michaels_url)
    return michaels_product

def acer(acer_url : str) -> dict:
    """Scrape product information from store.acer.com
    
    Keyword arguments:
    acer_url -- a product url from store.acer.com
    """
    acer_product = _acer._acer(acer_url)
    return acer_product

def walmart(walmart_url : str) -> dict:
    """Scrape product information from walmart.com
    
    Keyword arguments:
    walmart_url -- a product url from walmart.com
    """
    walmart_product = _walmart._walmart(walmart_url)
    return walmart_product

def adafruit(adafruit_url : str) -> dict:
    """Scrape product information from adafruit.com
    
    Keyword arguments:
    adafruit_url -- a product url from adafruit.com
    """
    adafruit_product = _adafruit._adafruit(adafruit_url)
    return adafruit_product

def xbox(xbox_url : str) -> dict:
    """Scrape product information from xbox.com
    
    Keyword arguments:
    xbox_url -- a product url from xbox.com
    """
    xbox_product = _xbox._xbox(xbox_url)
    return xbox_product

def joanns(joanns_url : str) -> dict:
    """Scrape product information from joanns.com
    
    Keyword arguments:
    joanns_url -- a product url from joanns.com
    """
    joanns_product = _joanns._joanns(joanns_url)
    return joanns_product

def github_shop(github_shop_url : str) -> dict:
    """Scrape product information from github.myshopify.com
    
    Keyword arguments:
    github_shop_url -- a product url from github.myshopify.com
    """
    github_shop_product = _github_shop._github_shop(github_shop_url)
    return github_shop_product

def macys(macys_url : str) -> dict:
    """Scrape product information from macys.com
    
    Keyword arguments:
    macys_url -- a product url from macys.com
    """
    macys_product = _macys._macys(macys_url)
    return macys_product

def chess_shop(chess_shop_url : str) -> dict:
    """Scrape product information from shop.chess.com
    
    Keyword arguments:
    chess_shop_url -- a product url from shop.chess.com
    """
    chess_shop_product = _chess_shop._chess_shop(chess_shop_url)
    return chess_shop_product

def newegg(newegg_url : str) -> dict:
    """Scrape product information from newegg.com
    
    Keyword arguments:
    newegg_url -- a product url from newegg.com
    """
    newegg_product = _newegg._newegg(newegg_url)
    return newegg_product

def etsy(etsy_url : str) -> dict:
    """Scrape product information from etsy.com
    
    Keyword arguments:
    etsy_url -- a product url from etsy.com
    """
    etsy_product = _etsy._etsy(etsy_url)
    return etsy_product

def overstock(overstock_url : str) -> dict:
    """Scrape product information from overstock.com
    
    Keyword arguments:
    overstock_url -- a product url from overstock.com
    """
    overstock_product = _overstock._overstock(overstock_url)
    return overstock_product

def pishop(pishop_url : str) -> dict:
    """Scrape product information from pishop.us
    
    Keyword arguments:
    pishop_url -- a product url from pishop.us
    """
    pishop_product = _pishop._pishop(pishop_url)
    return pishop_product

def boohoo(boohoo_url : str) -> dict:
    """Scrape product information from us.boohoo.com
    
    Keyword arguments:
    boohoo_url -- a product url from us.boohoo.com
    """
    boohoo_product = _boohoo._boohoo(boohoo_url)
    return boohoo_product