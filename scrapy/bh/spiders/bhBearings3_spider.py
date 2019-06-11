# scrape product info
# rem disable follow robot.txt 
'''
scrape product info from the buck & hickman web site

rem test spider:
    case 1:  scrape landing page (depth 1)
    case 2:  scrape landing page then depth 2
    case 3:  scrape landing page then depth n
    case 4:  scrape list of urls, then use it to
             scrape cases 2 and 3
'''
# imports  =========================================
import scrapy
import csv

# classes  =========================================
class bhBearings3_Spider(scrapy.Spider):
    name = "bhBearings3"
    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
    ]

    # master spider
    def parse(self, response):
        linkNames = []
        linkURLs = []
        
        linkList = response.css('ul.filter-box__list li.filter-box__item')[0]
        linkName = linkList.css('a::text')  # string with white space
        linkURL = linkList.css('a::attr(href)')  
        
        # populate parallel arrays for linkName / linkURL
        i = 0
        for item in linkName:
            n = linkName[i].get()
            u = linkURL[i].get()
            if n.find('Bearing') >= 0 and item != 'Bearings':
                linkNames.append(n.strip())
                linkURLs.append(u.strip())
            i += 1

        #for l in linkURLs:
        l = "https://www.buckandhickman.com/en/shop/products/results?page=1&category=87210&path=13-09"
        request = scrapy.Request(l, callback=self.parse_page1_info)
        yield request

    # parse product info for items on page 2
    def parse_page1_info(self, response):
        page = response.url

        pList = response.css('ul.list-view')
        pListItem = pList.css('li.list-view__item') 

        pInfo = pListItem.css('div.list-view__cell')
        pul = pInfo.css('ul.list-view__details')
        pli = pul.css('li.list-view__detail')

        i = 0
        for p in pListItem:
            #name = pInfo.css('h4 a::text')[i].get()
            yield { 
                'name': pInfo.css('h4 a::text')[i].get(), 
                'label': pli[i].css('p::attr(itemprop)').get(),
                'value': pli[i].css('p::attr(content)').get()
            }
            i += 1




# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()