# scrape product info
# rem disable follow robot.txt 
'''
quick spider to grab all brands for bh co.

'''
# imports  =========================================
import scrapy

# classes  =========================================
class bhBrands_Spider(scrapy.Spider):
    name = "bhBrands"
    start_urls = [
            "https://www.buckandhickman.com/en/shop/extended_search/brands",
    ]

    # master spider
    def parse(self, response):
        linkNames = response.css('ul.large-up-4 li.attributesItemCheckbox label input::attr(value)').getall()
        for name in linkNames:
            yield {
                'Brand': name,        
            }
         

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()