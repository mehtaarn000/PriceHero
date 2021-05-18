# -*- coding: utf-8 -*-

__version__ = "0.5.8"
__author__ = "mehtaarn000"
__license__ = "MIT"
__maintainer__ = "mehtaarn000"
__credits__ = ["mehtaarn000", "kilianalias", "nethracookie", "bizzyvinci"]
"""A python module that will allow users to get product prices information from a multitude of different websites."""
from . import (_amazon, _bestbuy, _dell, _michaels, _acer, _walmart, _adafruit,
               _xbox, _joann, _github_shop, _chess_shop, _newegg,
               _etsy, _overstock, _pishop, _boohoo, _walgreens,
               _whbm, _gucci, _louis_vuitton, _minecraft_shop, _ann_taylor,
               _tjmaxx, _journeys, _adidas, _lids, _jumia, _konga)


def amazon(amazon_url: str) -> dict:
    """Scrape product information from amazon.com

    Keyword arguments:
    amazon_url -- a product url from amazon.com
    """
    amazon_product = _amazon._amazon(amazon_url)
    return amazon_product


def bestbuy(bestbuy_url: str) -> dict:
    """Scrape product information from bestbuy.com
    
    Keyword arguments:
    bestbuy_url -- a product url from bestbuy.com
    """
    bestbuy_product = _bestbuy._bestbuy(bestbuy_url)
    return bestbuy_product


def dell(dell_url: str) -> dict:
    """Scrape product information from dell.com
    
    Keyword arguments:
    dell_url -- a product url from dell.com
    """
    dell_product = _dell._dell(dell_url)
    return dell_product


def michaels(michaels_url: str) -> dict:
    """Scrape product information from michaels.com
    
    Keyword arguments:
    michaels_url -- a product url from michaels.com
    """
    michaels_product = _michaels._michaels(michaels_url)
    return michaels_product


def acer(acer_url: str) -> dict:
    """Scrape product information from store.acer.com
    
    Keyword arguments:
    acer_url -- a product url from store.acer.com
    """
    acer_product = _acer._acer(acer_url)
    return acer_product


def walmart(walmart_url: str) -> dict:
    """Scrape product information from walmart.com
    
    Keyword arguments:
    walmart_url -- a product url from walmart.com
    """
    walmart_product = _walmart._walmart(walmart_url)
    return walmart_product


def adafruit(adafruit_url: str) -> dict:
    """Scrape product information from adafruit.com
    
    Keyword arguments:
    adafruit_url -- a product url from adafruit.com
    """
    adafruit_product = _adafruit._adafruit(adafruit_url)
    return adafruit_product


def xbox(xbox_url: str) -> dict:
    """Scrape product information from xbox.com
    
    Keyword arguments:
    xbox_url -- a product url from xbox.com
    """
    xbox_product = _xbox._xbox(xbox_url)
    return xbox_product


def joann(joann_url: str) -> dict:
    """Scrape product information from joann.com
    
    Keyword arguments:
    joann_url -- a product url from joann.com
    """
    joann_product = _joann._joann(joann_url)
    return joann_product


def github_shop(github_shop_url: str) -> dict:
    """Scrape product information from github.myshopify.com
    
    Keyword arguments:
    github_shop_url -- a product url from github.myshopify.com
    """
    github_shop_product = _github_shop._github_shop(github_shop_url)
    return github_shop_product


def chess_shop(chess_shop_url: str) -> dict:
    """Scrape product information from shop.chess.com
    
    Keyword arguments:
    chess_shop_url -- a product url from shop.chess.com
    """
    chess_shop_product = _chess_shop._chess_shop(chess_shop_url)
    return chess_shop_product


def newegg(newegg_url: str) -> dict:
    """Scrape product information from newegg.com
    
    Keyword arguments:
    newegg_url -- a product url from newegg.com
    """
    newegg_product = _newegg._newegg(newegg_url)
    return newegg_product


def etsy(etsy_url: str) -> dict:
    """Scrape product information from etsy.com
    
    Keyword arguments:
    etsy_url -- a product url from etsy.com
    """
    etsy_product = _etsy._etsy(etsy_url)
    return etsy_product


def overstock(overstock_url: str) -> dict:
    """Scrape product information from overstock.com
    
    Keyword arguments:
    overstock_url -- a product url from overstock.com
    """
    overstock_product = _overstock._overstock(overstock_url)
    return overstock_product


def pishop(pishop_url: str) -> dict:
    """Scrape product information from pishop.us
    
    Keyword arguments:
    pishop_url -- a product url from pishop.us
    """
    pishop_product = _pishop._pishop(pishop_url)
    return pishop_product


def boohoo(boohoo_url: str) -> dict:
    """Scrape product information from us.boohoo.com
    
    Keyword arguments:
    boohoo_url -- a product url from us.boohoo.com
    """
    boohoo_product = _boohoo._boohoo(boohoo_url)
    return boohoo_product


def walgreens(walgreens_url: str) -> dict:
    """Scrape product information from walgreens
    
    Keyword arguments:
    walgreens_url -- a product url from walgreens.com
    """
    walgreens_product = _walgreens._walgreens(walgreens_url)
    return walgreens_product


def whbm(whbm_url: str) -> dict:
    """Scrape product information from White House Black Market
    
    Keyword arguments:
    whbm_url -- a product url from whitehouseblackmarket.com
    """
    whbm_product = _whbm._whbm(whbm_url)
    return whbm_product


def gucci(gucci_url: str) -> dict:
    """Scrape product information from Gucci
    
    Keyword arguments:
    gucci_url -- a product url from gucci.com
    """
    gucci_product = _gucci._gucci(gucci_url)
    return gucci_product


def louis_vuitton(louis_vuitton_url: str) -> dict:
    """Scrape product information from Louis Vuitton
    
    Keyword arguments:
    louis_vuitton_url -- a product url from us.louisvuitton.com
    """
    louis_vuitton_product = _louis_vuitton._louis_vuitton(louis_vuitton_url)
    return louis_vuitton_product


def minecraft_shop(minecraft_url: str) -> dict:
    """Scrape product information from Minecraft Shop
    
    Keyword arguments:
    minecraft_url -- a product url from shop.minecraft.net
    """
    minecraft_product = _minecraft_shop._minecraft_shop(minecraft_url)
    return minecraft_product


def ann_taylor(ann_taylor_url: str) -> dict:
    """Scrape product information from Ann Taylor
    
    Keyword arguments:
    ann_taylor_url -- a product url from anntaylor.com
    """
    ann_taylor_product = _ann_taylor._ann_taylor(ann_taylor_url)
    return ann_taylor_product


def tjmaxx(tjmaxx_url: str) -> dict:
    """Scrape product information from Tjmaxx
    
    Keyword arguments:
    tjmaxx_url -- a product url from tjmaxx.tjx.com
    """
    tjmaxx_product = _tjmaxx._tjmaxx(tjmaxx_url)
    return tjmaxx_product


def journeys(journeys_url: str) -> dict:
    """Scrape product information from Journeys
    
    Keyword arguments:
    journeys_url -- a product url from journeys.com
    """
    journeys_product = _journeys._journeys(journeys_url)
    return journeys_product


def adidas(adidas_url: str) -> dict:
    """Scrape product information from Adidas
    
    Keyword arguments:
    adidas_url -- a product url from adidas.com
    """
    adidas_product = _adidas._adidas(adidas_url)
    return adidas_product


def lids(lids_url: str) -> dict:
    """Scrape product information from Lids
    
    Keyword arguments:
    lids_url -- a product url from lids.com
    """
    lids_product = _lids._lids(lids_url)
    return lids_product


def jumia(jumia_url: str) -> dict:
    """Scrape product information from jumia
    
    Keyword arguments:
    jumia_url -- a product url from jumia.com.*
    """
    jumia_product = _jumia._jumia(jumia_url)
    return jumia_product


def konga(konga_url: str) -> dict:
    """Scrape product information from konga
    
    Keyword arguments:
    konga_url -- a product url from konga.com
    """
    konga_product = _konga._konga(konga_url)
    return konga_product
