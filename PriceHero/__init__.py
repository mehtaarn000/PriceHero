from websites.amazon import amazon as a
from websites.bestbuy import bestbuy as b
from websites.dell import dell as d
from websites.michaels import michaels as e
from websites.acer import acer as f
from websites.walmart import walmart as g
from websites.adafruit import adafruit as h
from websites.xbox import xbox as i
from websites.joanns import joanns as j
from websites.github_shop import github_shop as k
from websites.macys import macys as l

def amazon(self):
    amazon_product = a(self)
    return amazon_product

def bestbuy(self):
    bestbuy_product = b(self)
    return bestbuy_product

def dell(dell_url):
    dell_product = d(dell_url)
    return dell_product

def michaels(michaels_url):
    michaels_product = e(michaels_url)
    return michaels_product

def acer(acer_url):
    acer_product = f(acer_url)
    return acer_product

def walmart(walmart_url):
    walmart_product = g(walmart_url)
    return walmart_product

def adafruit(adafruit_url):
    adafruit_product = h(adafruit_url)
    return adafruit_product

def xbox(xbox_url):
    xbox_product = i(xbox_url)
    return xbox_product

def joanns(joanns_url):
    joanns_product = j(joanns_url)
    return joanns_product

def github_shop(github_shop_url):
    github_shop_product = k(github_shop_url)
    return github_shop_product

def macys(macys_url):
    macys_product = l(macys_url)
    return macys_product