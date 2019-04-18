# scrapy_tester.py
# getting started with a scrapy web scraper


# imports  =========================================
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re # regular expression library


# main     =========================================
def main():
	# point to html markup doc
	htmlDoc = open('DSFD_Listing.html', 'rt')

	# make a BeautifulSoup object, and then let it turn the 
	# html markup from htmldoc into a parse tree
	soup = BeautifulSoup(htmlDoc, 'html.parser')
	htmlDoc.close()

	# print some stuff from the markup
	print(soup.prettify()[0:200])
	print('\n\n')
	print(soup.p.attrs)
	print(soup.body.p)

	# point to web page
	myPage = 'https://analytics.usa.gov'

	# make a BeautifulSoup object, and then let it turn the
	# html from the page into a parse tree
	p = urllib.request.urlopen(myPage)
	# urllib.request.urlopen('https://analytics.usa.gov').read()
	soup = BeautifulSoup(p, 'html.parser')

	# print some stuff from the url
	print('\n\n')
	print(soup.prettify()[0:200])

	# print all <a> tags from the page
	print('\n', 'Printing all href links in all <a> tags:', '\n')
	for link in soup.find_all('a'):print(link.get('href'))

	print('\n', 'Printing all <a> tags with attr of http:', '\n')
	# print all <a> tags from page that have attribute of href
	for link in soup.findAll('a', attrs = {'href':re.compile('http')}): print(link)

	# output results to external file
	print('\n', 'Printing to external file', '\n')
	outfile = open('parsedData.txt', 'wt')
	for link in soup.findAll('a', attrs = {'href':re.compile('http')}): 
		soup_link = str(link)
		#print (soup_link)
		outfile.writelines(soup_link)
		outfile.writelines('\n')
	outfile.flush()
	outfile.close()

if __name__ == '__main__': main()