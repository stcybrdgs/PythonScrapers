# gq2_spider.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class homDep1_Spider(scrapy.Spider):
    name = "homDep1"

    start_urls = [
            'https://www.granquartz.com/stone-fabrication/power-tools-accessories',
        ]
        
    def parse(self, response):
        for item in response.css('div.block-product._list'):
            yield {
'''
storeList = response.css('section.grid ul.storeList')
address = storeList.css('li.storeList__item ul.storeList__details li::text')[0]
cityStateZip = storeList.css('li.storeList__item ul.storeList__details li::text')[1].get()
phone = storeList.css('li.storeList__item ul.storeList__details li::text')[2]

'storeList' : response.css('section.grid ul.storeList').get(),
'Address' : storeList.css('li.storeList__item ul.storeList__details li::text')[0].get(),
'CityStateZip' : storeList.css('li.storeList__item ul.storeList__details li::text')[1].get(),
'Phone' : storeList.css('li.storeList__item ul.storeList__details li::text')[2].get(),
'''
                'Product': item.css('div.product-block-pad a::text').get().strip(),
                'Sku': item.css('div.product-block-pad p.sku::text').get(),
                'Price': item.css('div.price-box span.price::text').get(),
            }
            
        nextPage = response.css('li.pages-item-next a::attr(href)').get()
        if nextPage is not None:
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()