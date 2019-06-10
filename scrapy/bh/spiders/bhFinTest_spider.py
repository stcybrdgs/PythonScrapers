# scrape product info
# rem disable follow robot.txt 
'''
    case 1:  scrape page
    case 2:  scrape page + depth 1
    case 3:  scrape page + depth 1 + depth 2
    case 4:  scrape page 1 for href array and use it
             to scrape case 2 and case 3
    case 5:  any of the above cases output to csv
             per import csv
'''

# imports  =========================================
import scrapy


# classes  =========================================
class bhFinTest_Spider(scrapy.Spider):
    name = "bhFinTest"
    start_urls = [
            'http://quotes.toscrape.com',
        ]

    # master spider
    def parse(self, response):
        linkList = response.css('div.tags-box')
        link = linkList.css('span.tag-item a::attr(href)')
        href = 'http://quotes.toscrape.com' 
        links = []
        
        # populate links list with links to be scraped
        for l in link.getall():
            nuhref = href + l
            links.append(nuhref)
        
        # call secondary parsing functions to parse
        # responses from calls to links in the list of links
        for l in links:
            # call secondary parsing function...
            request = scrapy.Request(l, callback=self.parse_quote)
            
            # output data from the secondary parsing function
            yield request
        
    # secondary parsing function to process list of links    
    def parse_quote(self, response):
        page = response.url
        quote = response.css('span::text').get()
        yield { 
            'url': page,
            'quote': quote,
        }

# main     =========================================
def main():
    print('Done.')

if __name__ == '__main__': main()