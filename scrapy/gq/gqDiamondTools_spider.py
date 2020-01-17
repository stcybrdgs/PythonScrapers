# gq2_spider.py
"""
Thur Jan 16, 2020
Stacy Bridges

Scraping the GranQuartz online catalog for product data related to pads:
    - Brand Name    |  Diamax
    - Product Type  |  Granite Polishing Pad
    - Group         |
    - Product Name  |  Typhoon 7Step Diamond Granite Wet Polishing Pad 4" 50 grit
    - Size          |  4"
    - Grit          |  50
    - Price         |  $

"""

# imports  =====================================================================
import os, sys
import scrapy

# classes  =====================================================================
class GQDiamondTools_Spider(scrapy.Spider):
    name = "gqDiamondTools"
    start_urls = ['https://www.granquartz.com/concretes/diamond-tools-abrasives']

    # LEVEL 1 PAGE  --------------------------------------------------------
    def parse(self, response):
        pad_urls = []
        pad_urls_unq = []

        # GET THE ARRAY OF HYPERLINKS  -----------------------------------------
        # get all unique product hrefs from current web page and add them to pad_urls[]
        re = response.css('div.products-wrap').css('a::attr(href)').getall()
        for item in re:
            if item not in pad_urls_unq and item.find("https://") >= 0:
                pad_urls_unq.append(item)
                pad_urls.append(item)

        # follow the links in pad_urls[] to go to the next page and scrape the product data;
        # when the data is returned from the LEVEL 2 PAGE, yield it to the output channel
        for pu in pad_urls:
            yield scrapy.Request(pu, callback=self.get_product_data)

        # look for a 'nextpage' hyperlink and set it to empty if there isn't one
        try:
            next = response.css("li.pages-item-next a.next::attr('href')").get()
        except:
            next = ''

        # if there is a 'nextpage' hyperlink, follow it by running parse() recursively
        if len(next) > 0:
            url = response.urljoin(next)
            yield scrapy.Request(url, self.parse)

    # LEVEL 2 PAGE  --------------------------------------------------------
    # scrape the product data and return it to the caller
    def get_product_data(self, response):
        re2 = response.css('div.table-wrapper')
        product_names = re2.css('table.data td strong.product-item-name::text').getall()
        product_ids = re2.css('table.data td span.product-item-epicor-id::text').getall()
        product_prices = re2.css('table.data td div.price-box span.price::text').getall()

        i = 0
        for productName in product_names:
            yield{
                'Product Name': productName,
                'Product ID': product_ids[i],
                'Product Prices': product_prices[i]
            }
            i += 1

# main  ========================================================================
def main():
	print('Done.')

if __name__ == '__main__': main()
