# scrape product info
# rem disable follow robot.txt 

# imports  =========================================
import scrapy
# import csv

# classes  =========================================
class bhBearings_Spider(scrapy.Spider):
    name = "bhBearings"

    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
        ]
    
    def parse(self, response):
        crawlBlock = response.css('div.filter-box__block ul.filter-list li.filter-list__item')
        productLinks = crawlBlock.css('a.filter-list__link::text').getall()
        
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
        
        for item in productLinks:
            if item.strip() in bearingProducts: 
                scrapedInfo = {
                    # key: value
                    'productGroups': item.strip()
                }
        
                # yield scraped info to scrapy
                yield scrapedInfo
        
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