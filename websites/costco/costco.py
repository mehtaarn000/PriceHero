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
    productdata = {"price":"", "name":""}
    return productdata
    driver.quit()
