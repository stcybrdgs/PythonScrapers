# gq2_spider.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class homDep1_Spider(scrapy.Spider):
    name = "homDep1"

    start_urls = [
            'https://www.homedepot.com/l/TX',
        ]
        
    def parse(self, response):
        for item in response.css('section.grid ul.storeList'):
            yield {
                    'storeList' : response.css('section.grid ul.storeList').get(),
                    'Address' : item.css('li.storeList__item ul.storeList__details li::text')[0].get(),
                    'CityStateZip' : item.css('li.storeList__item ul.storeList__details li::text')[1].get(),
                    'Phone' : item.css('li.storeList__item ul.storeList__details li::text')[2].get(),
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