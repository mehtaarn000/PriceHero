from amazon import amazon as a
from bestbuy import bestbuy as b
from costco import costco as c
from dell import dell as d
from michaels import michaels as e
from acer import acer as f

def amazon(self):
    amazon_product = a(self)
    return amazon_product

def bestbuy(self):
    bestbuy_product = b(self)
    return bestbuy_product
    
def costco(self):
    costco_product = c(self)
    return costco_product

def dell(dell_url):
    dell_product = d(dell_url)
    return dell_product

def michaels(michaels_url):
    michaels_product = e(michaels_url)
    return michaels_product

def acer(acer_url):
    acer_product = f(acer_url)
    return acer_product