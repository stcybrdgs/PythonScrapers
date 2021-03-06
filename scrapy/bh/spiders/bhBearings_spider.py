# scrape product info
# rem disable follow robot.txt 

# imports  =========================================
import scrapy
# import csv

# classes  =========================================
class bhBearings_Spider(scrapy.Spider):
    name = "bhBearings"
    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/results?page=1&category=87210&path=13-09',
            #'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
    ]
    
    def parse(self, response):
        productsBlockList = response.css('div.filter-box__wrapper section.block')
        productList = productsBlockList.css('ul.list-view') # count = 1
        productListItem = productList.css('li.list-view__item') # count = 24
        #productCell = productListItem.css('article div.list-view__cell') # count = 47
        
        #i = 0
        for item in productListItem:
            yield {
                    'ProductName' : item.css('h4 a::text').get(),
                    'OrderCode' : item.css('ul.list-view__details li strong::text')[0].get(),
                    'Brand' : item.css('ul.list-view__details li strong::text')[1].get(),
                    'MfrPartNo' : item.css('ul.list-view__details li strong::text')[2].get(),
            }
            '''
            'OrderCode' : item.css('ul.list-view__details li strong::text')[0].get(),
            'Brand' : item.css('ul.list-view__details li strong::text')[1].get(),
            'MfrPartNo' : item.css('ul.list-view__details li strong::text')[2].get(),
            '''            
            #i += 1
        
        '''
        crawlBlock = response.css('div.filter-box__block ul.filter-list li.filter-list__item')
        allProductGroups = crawlBlock.css('a.filter-list__link::text').getall()
        allProductLinks = crawlBlock.css('a.filter-list__link::attr(href)').getall()
        productType = 'Bearing'  # search term
        scrapedInfo = {}
        # groupList = []  #list of group names
        # linkList = []  # list of links for each group name
        # create at array of links that pertain to bearing products
        # if the product group contains the name 'bearing'
        # then put the corresponding link into the link array
        '''
        
        '''
        the links we want are:
        'Combined Thrust Radial Bearings', 'Plain Bearings', 
        'Radial Ball Bearings', 'Radial Needle Roller Bearings',
        'Radial Roller Bearings', 'Thrust (Axial) Ball Bearings',
        'Thrust (Axial) Needle Roller Bearings',
        'Thrust (Axial) Roller Bearings', 'Track Runner Bearings',
        '''
        '''
        i = 0
        for item in allProductGroups:
            if item.find(productType) >= 0:
                scrapedInfo[item.strip()] = allProductLinks[i]
            i += 1
        
        # yield scraped info to scrapy
        yield scrapedInfo
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