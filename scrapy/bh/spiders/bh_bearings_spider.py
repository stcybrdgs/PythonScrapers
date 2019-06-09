# homDep1_spider.py
# scrape locations of Home Depot Stores in Texas
# rem disable follow robot.txt 

# imports  =========================================
import scrapy

# classes  =========================================
class bhBearings_Spider(scrapy.Spider):
    name = "bhBearings"

    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
        ]

    # identify the bearing products that we'd like to scrape        
    bearingProducts = [
        'Combined Thrust Radial Bearings',
        'Plain Bearings',
        'Radial Ball Bearings',
        'Radial Needle Roller Bearings',
        'Radial Roller Bearings',
        'Thrust (Axial) Ball Bearings',
        'Thrust (Axial) Needle Roller Bearings',
        'Thrust (Axial) Roller Bearings',
        'Track Runner Bearings',
            ]
    def parse(self, response):
        
        crawlBlock = response.css('div.filter-box__block ul.filter-list li.filter-list__item')
        productLinks = crawlBlock.css('a.filter-list__link::text').getall()
        for i in productLinks:
            yield{
                'productLink': i.strip()
           }
        
        '''
        for link in crawlBlock:
            yield {
                'productLink': crawlBlock.css('a.filter-list__link::text').get(),
            }
        '''
        
        '''
        bearingProducts = crawlBlock.css('a.filter-list__link::text').getAll()
        for i in bearingProducts: print(i.strip())
        '''
                
        '''
        crawlBlock = response.css('section.grid')[0]
        crawlDiv = crawlBlock.css('div.col__12-12')[1]
        storeList = crawlDiv.css('ul.storeList')
        storeListItem = storeList.css('li.storeList__item')
        # storeListItem = storeList.css('li.storeList__item')
        count = 0 # sentinel val
        for item in storeListItem:
            yield {
                'City' : item.css('a::text').get(),
                'Address' : item.css('ul.storeList__details li::text')[0].get(),
                'CityStateZip' : item.css('ul.storeList__details li::text')[1].get(),
                'Phone' : item.css('ul.storeList__details li::text')[2].get(),
            }
            count += 1
        '''
            
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