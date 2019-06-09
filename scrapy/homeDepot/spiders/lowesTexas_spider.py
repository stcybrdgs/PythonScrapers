# lowesTexas_spider.py
# scrape locations of Home Depot Stores in Texas


# imports  =========================================
import scrapy

# classes  =========================================
class lowesTX_Spider(scrapy.Spider):
    name = "lowesTX"

    start_urls = [
            'https://www.lowes.com/Lowes-Stores/Texas/TX',
        ]
        '''
    landing page:

        city:
        div.storedirectory ul.category-list li.mobile-grid-100 span

        branch-name:
        div.storedirectory ul.category-list li.mobile-grid-100 span a

        branch-link:
        div.storedirectory ul.category-list li.mobile-grid-100 span a:attr(href)
        
    linked page:
        city:
        section.store-detail-desktop div.grid-100 h1.js-store-detail-pageTitle
     
        address:
        ibid
        div.store div.address address span 
        itemprop 'streetAddress'
        span.white

        city: span itemprop 'addressLocality'
        state: span itemprop 'addressRegion'
        span itemprop 'postalCode'

        store-number:: span.white::text



        state:
        zip-code:
        store-phone:
        pro-service-desk:






        '''
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