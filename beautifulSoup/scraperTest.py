# scraperTest.py
# testing a python/beautifulSoup screen scraper

# import libraries
import urllib.request
import urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
# where <h1 class="companyName__99a4824b">S&amp;P 500 Index</h1>
name_box = soup.find('h1', attrs={'class': 'name'})

# now that you have the tag, get the data out of it as text
# and use strip() to remove starting and trailing
name = name_box#.innerHTML.strip() 
print (name_box)
