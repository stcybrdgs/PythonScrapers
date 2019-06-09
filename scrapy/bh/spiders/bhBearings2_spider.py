# scrape product info
# rem disable follow robot.txt 

# imports  =========================================
import scrapy
# import csv

# classes  =========================================
class bhBearings_Spider(scrapy.Spider):
    name = "bhBearings2"
    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
    ]

    def parse(self, response):
        # linkListItemNames = []
        # linkListItemURLs = []
        
        allLinkLists = response.css('ul.filter-box__list li.filter-box__item')
        linkList = allLinkLists[0]
        linkName = linkList.css('a::text')  # string with white space
        linkURL = linkList.css('a::attr(href)')  
        
        
        i = 0
        for item in linkName:
            n = linkName[i].get()
            u = linkURL[i].get()
            # linkListItemNames.append(n.strip())
            # linkListItemURLs.append(u.strip())
            yield{
                    'Product Name' : n.strip(),
                    'Product Link' : u.strip(),
            }
            i += 1

            
        
            '''prin
            yield {
                    'ProductName' : item.css('h4 a::text').get(),
                    'OrderCode' : item.css('ul.list-view__details li strong::text')[0].get(),
                    'Brand' : item.css('ul.list-view__details li strong::text')[1].get(),
                    'MfrPartNo' : item.css('ul.list-view__details li strong::text')[2].get(),
            }
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