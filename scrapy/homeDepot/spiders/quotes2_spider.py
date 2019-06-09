# quotes_spider_2.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class QuotesSpider(scrapy.Spider):
    # identify the spider
    name = "quotes2"

    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()