# gq1_spider.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class GQ1_Spider(scrapy.Spider):
    name = "gq1"

    start_urls = [
            'https://www.granquartz.com/stone-fabrication/power-tools-accessories',
        ]
        
    '''
    FEED_FORMAT: jsonlines
    Exporter used: JsonLinesItemExporter
    URI scheme: file
    Example URI: file:///tmp/export.csv
    
    productsWrap = response.css('div.block-product._list')
    // productDiv = productsWrap.css('div.product-block-pad')
    productName = productsWrap.css('div.product-block-pad a::text')
    productSku = productsWrap.css('div.product-block-pad p.sku::text')
    // priceDiv = productsWrap.css('div.price-box')
    price = productsWrap.css('div.price-box span.price::text')
    
    def parse(self, response):
        for item in response.css('div.products-wrap'):
            yield {
                'Product': item.css('div.product-block-pad a::text').getall(),
                'Sku': item.css('div.product-block-pad p.sku::text').get(),
                'Price': item.css('div.price-box span.price::text').get()
            
            }
    '''
        
    def parse(self, response):
        for item in response.css('div.block-product._list'):
            yield {
                'Product': item.css('div.product-block-pad a::text').get(),
                'Sku': item.css('div.product-block-pad p.sku::text').get(),
                'Price': item.css('div.price-box span.price::text').get(),
            }

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()