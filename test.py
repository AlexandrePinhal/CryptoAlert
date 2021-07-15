

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import re

# url of the source
urlpage = 'https://www.coindesk.com/en/price/bitcoin'

page = urllib.request.urlopen(urlpage) #return the thml to the variable page
soup = BeautifulSoup(page, 'html.parser') #use beautifulsoup to analyse html

price = (soup.find("div", {"class": "price-large"}).getText())
price = price[1:]
print(price)
finalprice= price.replace(",", "")
print(int(float(finalprice)))
