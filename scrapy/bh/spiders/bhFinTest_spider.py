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
import csv


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
        
        # print('==============================================')
        # print('==============================================')

        # call secondary parsing functions to parse
        # responses from calls to links in the list of links
        for l in links:
            request = scrapy.Request(l, callback=self.parse_quotes)
            yield request
        
    # secondary parsing function to process list of links    
    def parse_quotes(self, response):
        page = response.url
        quote = response.css('span::text').get()
        
        # write output to csv file
        with open('bhTester_flat.csv', mode='a') as tester_file:
            tester_writer = csv.writer(tester_file, delimiter=',',
                quotechar = '"', quoting=csv.QUOTE_MINIMAL)
            tester_writer.writerow([page, quote])

        # tester_file.close()
        
        # send dictionary back to caller
        yield { 
            'url': page,
            'quote': quote,
        }

# main     =========================================
def main():
    print('Done.')

if __name__ == '__main__': main()