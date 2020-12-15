# PriceHero
A python module that will allow users to get product prices information from a multitude of different websites. 

## Installation
`pip install PriceHero-mehtaarn000`

## Usage
Import the module with:

`import PriceHero as ph`

Now, scrape a product off acer with:

`laptop = ph.acer(https://store.acer.com/en-us/aspire-5-laptop-a515-56-55j8)`

After you `print(laptop)`, your output should be something like this:

`{'price': '$649.99', 'name': 'Aspire 5 Laptop - A515-56-55J8', 'discountprice': None}`

## Supported Websites
1. Amazon
2. Acer
3. Dell
4. Michaels
5. BestBuy
6. Walmart
7. Joanns
8. Home Depot
9. Adafruit
10. Xbox
11. Github Shop
12. Macys
