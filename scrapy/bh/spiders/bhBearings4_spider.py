# scrape product info
# rem disable follow robot.txt 
'''
scrape product info from the buck & hickman web site

rem test spider:
    case 1:  scrape landing page (depth 1)
    case 2:  scrape landing page then depth 2
    case 3:  scrape landing page then depth n
    case 4:  scrape list of urls, then use it to
             scrape cases 2 and 3
'''
# imports  =========================================
import scrapy
import csv

# classes  =========================================
class bhBearings4_Spider(scrapy.Spider):
    name = "bhBearings4"
    start_urls = [
            'https://www.buckandhickman.com/en/shop/products/categories/Bearings/13/84888',
    ]

    # master spider
    def parse(self, response):
        linkNames = []
        linkURLs = []
        
        linkList = response.css('ul.filter-box__list li.filter-box__item')[0]
        linkName = linkList.css('a::text')  # string with white space
        linkURL = linkList.css('a::attr(href)')  
        
        # populate parallel arrays for linkName / linkURL
        i = 0
        for item in linkName:
            n = linkName[i].get()
            u = linkURL[i].get()
            if n.find('Bearing') >= 0 and item != 'Bearings':
                linkNames.append(n.strip())
                linkURLs.append(u.strip())
            i += 1

        #for l in linkURLs:
        l = "https://www.buckandhickman.com/en/shop/products/results?page=1&category=87210&path=13-09"
        request = scrapy.Request(l, callback=self.parse_page1_info)
        yield request

    # parse product info for items on page 2
    def parse_page1_info(self, response):
        page = response.url
        pListBox = response.css('ul.list-view li.list-view__item') 
        pName = pListBox.css('h4 a::text')
        pAttrBox = pListBox.css('div.row ul.list-view__details')
        pAttrKey = pAttrBox.css('p::attr(itemprop)')
        pAttrVal = pAttrBox.css('p::attr(content)')

        '''
        # to retrieve all names:
        i = 0
        for p in pListBox:
            print(pName[i].get())
            i += 1

        # to retrieve all sets of [sku, brand, mpn]:
        i = 0
        for p in pAttrBox:
            print(pAttrBox[i].get())
            i += 1

        # to retrieve all keys:
        i = 0
        for key in pAttrBox:
            print(pAttrKey[i].get())
            i += 1

        # to retrieve all values:
        i = 0
        for val in pAttrBox:
            print(pAttrVal[i].get())
            i += 1            
        '''
        i = 0
        j = 0
        attrList = ['sku', 'brand', 'mpn']

        for pItem in pListItem:
            product = pInfo.css('h4 a::text')[i].get()
            sku = ''
            brand = ''
            mpn = ''

            for uItem in pul:
                itemprop = pli[j].css('p::attr(itemprop)').get()
                content = pli[j].css('p::attr(content)').get()

                if itemprop in attrList:
                    if itemprop == 'sku': sku = content
                    elif itemprop == 'brand': brand = content
                    elif itemprop == 'mpn': mpn = content
                # end if
                j += 1
            # end for

            yield { 
                'Product': product, 
                'SKU': sku,
                'Brand': brand,
                'MfrPartNo': mpn
            }
            i += 1
        # end for 
         

# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()