def amazon(amazon_website):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    actual_amazon_website = driver.get(amazon_website)
    amazon_price = driver.find_element_by_xpath('//*[@id="price_inside_buybox"]')
    print(amazon_price.text)
    driver.close()