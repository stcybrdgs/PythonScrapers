# quotes3_spider.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class QuotesSpider(scrapy.Spider):
    # identify the spider
    # for this spider, the parse() method will be called
    # to handle each of the urls in the url array even though
    # it is not explicitly called--> rem parse() is Scrapy's
    # default callback method
    name = "quotes3"

    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()