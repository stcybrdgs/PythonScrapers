# scrape product info
# rem disable follow robot.txt 
'''
    case 1:  scrape page
    case 2:  scrape page + depth 1
    case 3:  scrape page + depth 1 + depth 2
    case 4:  scrape page 1 for href array and use it
             to scrape case 2 and case 3
'''

# imports  =========================================
import scrapy
# import csv


# globals  =========================================


# classes  =========================================

class bhTester_Spider(scrapy.Spider):
    name = "bhTester"
    start_urls = [
            'http://quotes.toscrape.com',
        ]

    def parse(self, response):
        linkList = response.css('div.tags-box')
        link = linkList.css('span.tag-item a::attr(href)')
        quote = response.css('span::text').get()
        links = []

        for l in link.getall():
            href = 'http://quotes.toscrape.com' + l
            links.append(href)
        
            yield{
                'url': l,
                'quote': quote,
            }
       
        
        
# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()