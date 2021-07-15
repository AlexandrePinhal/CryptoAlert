

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import re

# url of the source
urlpage = 'https://www.coindesk.com/en/price/bitcoin'

page = urllib.request.urlopen(urlpage) #return the thml to the variable page
soup = BeautifulSoup(page, 'html.parser') #use beautifulsoup to analyse html

price = (soup.find_all("div", {"class": "price-large"}))
price_string = str(price)
print(type(price_string))

temp = re.findall(r'\d+', price_string)
res = list(map(int, temp))
res = str(res)
res2 = "".join(res)
print(res2)