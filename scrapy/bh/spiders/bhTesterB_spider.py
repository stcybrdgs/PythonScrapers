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
        href = 'http://quotes.toscrape.com' 

        for l in link.getall():
            nuhref = href + l
            links.append(nuhref)
        
        for l in links:
            yield{
                'href': l,
                'quote': quote,
            }

        print('HERE IS WHERE THE COOKIE CRUMBLE CRACKS!!')
        request = scrapy.Request("http://quotes.toscrape.com/tag/simile/",
                                 callback=self.parse_quote)
        yield request
        yield{
            'quote': request
        }

    def parse_quote(self, response):
        data = response.css('span::text').get()
        yield data
        yield{
            'quote': data
        }
        
        
# main     =========================================
def main():
    print('Done.')

if __name__ == '__main__': main()