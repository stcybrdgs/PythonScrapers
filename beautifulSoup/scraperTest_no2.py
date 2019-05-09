# scraperTest_no2.py
# testing a python/beautifulSoup screen scraper

import requests
from selenium import webdriver

'''
result = requests.get('https://wrangleworks.com')
page = result.text
print(page)
'''

driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/')
page = driver.page_source


