# PriceHero
A python module that will allow users to get product prices information from a multitude of different websites. 
[pypi link](https://pypi.org/project/PriceHero-mehtaarn000/)

## Installation
`pip install PriceHero-mehtaarn000`

## Example
Import the module with:

`import PriceHero as ph`

Now, scrape a product off acer with:

`laptop = ph.acer("https://store.acer.com/en-us/aspire-5-laptop-a515-56-55j8")`

After you `print(laptop)`, your output should be something like this:

`{'price': '$649.99', 'name': 'Aspire 5 Laptop - A515-56-55J8', 'discountprice': None}`

## Supported Websites
Total of 19!
- Amazon
- Acer
- Dell
- Michaels
- BestBuy
- Walmart
- Joanns
- Adafruit
- Xbox
- Github Shop
- Macys
- Chess.com Shop
- Newegg
- Etsy
- Overstock
- Pishop
- Boohoo
- Walgreens
- Forever21