# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

# url of the source
urlpage = 'https://bitcoin.fr/le-cours-du-bitcoin/'

page = urllib.request.urlopen(urlpage) #return the thml to the variable page
soup = BeautifulSoup(page, 'html.parser') #use beautifulsoup to analyse html

#print(soup)

cryptoprice = soup.find_all(data-currency="EUR")[0].get_text()
print(cryptoprice)