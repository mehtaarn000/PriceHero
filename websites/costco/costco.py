def costco(costco_url):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    website = driver.get(costco_url)
    website
    costco_price = driver.find_element_by_class_name('value')
    costco_name = driver.find_element_by_css_selector('#product-details > div.row.visible-lg.visible-xl > div > div.product-h1-container-v2.visible-lg-block.visible-xl-block > h1')
    print('$', costco_price.text)
    print(costco_name.text)
    driver.quit()

costco('https://www.costco.com/apple-mac-mini---intel-core-i3---8gb-memory---256gb-ssd.product.100531970.html')