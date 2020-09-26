from websites.amazon import amazon as a
from websites.bestbuy import bestbuy as b
from websites.dell import dell as d
from websites.michaels import michaels as e
from websites.acer import acer as f
from websites.walmart import walmart as g
from websites.adafruit import adafruit as h

def amazon(self):
    amazon_product = a.amazon(self)
    return amazon_product

def bestbuy(self):
    bestbuy_product = b.bestbuy(self)
    return bestbuy_product

def dell(dell_url):
    dell_product = d.dell(dell_url)
    return dell_product

def michaels(michaels_url):
    michaels_product = e.michaels(michaels_url)
    return michaels_product

def acer(acer_url):
    acer_product = f.acer(acer_url)
    return acer_product

def walmart(walmart_url):
    walmart_product = g.walmart(walmart_url)
    return walmart_product

def adafruit(adafruit_url):
    adafruit_product = h.adafruit(adafruit_url)
    return adafruit_product
