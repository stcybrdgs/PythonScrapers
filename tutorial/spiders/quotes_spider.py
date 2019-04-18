# quotes_spider.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class QuotesSpider(scrapy.Spider):
    # identify the spider
    name = "quotes"

    # rem: 
    # create an iterable of urls to crawl
    # spider can crawl a list of requests
    # starting from static list or generator function
    def start_requests(self):
        # use static list of urls for the spider to crawl
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            # return a scrapy.Request object
            yield scrapy.Request(url=url, callback=self.parse)

    # create a method to handle responses from requests
    # that are being crawled
    # (the parse() method usually parses the response, 
    #   extracts the scraped data as dicts, and
    #   finds new URLs to follow by creating new requests from them)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()