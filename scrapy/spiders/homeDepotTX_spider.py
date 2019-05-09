# homeDepot-TX_spider.py
# scrape locations of Home Depot Stores in Texas


# imports  =========================================
import scrapy

# classes  =========================================
class homeDepotTX_Spider(scrapy.Spider):
    name = "homeDepotTX"

    start_urls = [
            'https://www.homedepot.com/l/TX',
        ]
        
    def parse(self, response):
        crawlBlock = response.css('section.grid')[0]
        crawlDiv = crawlBlock.css('div.col__12-12')[1]
        storeList = crawlDiv.css('ul.storeList')
        storeListItem = storeList.css('li.storeList__item')
        # storeListItem = storeList.css('li.storeList__item')
        for item in storeListItem:
            yield {
                'City' : item.css('a::text').get(),
                'Address' : item.css('ul.storeList__details li::text')[0].get(),
                'CityStateZip' : item.css('ul.storeList__details li::text')[1].get(),
                'Phone' : item.css('ul.storeList__details li::text')[2].get()
            }
            
        '''
        nextPage = response.css('li.pages-item-next a::attr(href)').get()
        if nextPage is not None:
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)
        '''
        
# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()