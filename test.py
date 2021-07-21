

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import telegram
from time import *


                             ### GETTING THE PRICE ###

# url of the source
urlpage = 'https://www.coindesk.com/en/price/bitcoin'

page = urllib.request.urlopen(urlpage) #return the html to the variable page
soup = BeautifulSoup(page, 'html.parser') #use beautifulsoup to analyse html

price = (soup.find("div", {"class": "price-large"}).getText())
price = price[1:]
finalprice= price.replace(",", "")
print(int(float(finalprice)))

                            ### SENDING A TELEGRAM CHAT ###

def Telechat():
    if (finalprice) < "30000" and (finalprice) > "25000" :
        pass
    else:
        my_token = '1846958060:AAH0vB6Su8bhRVDXM78BVqhYYjIWyp-gQzc'

        def send(msg, chat_id, token=my_token):
            bot = telegram.Bot(token=token)
            bot.sendMessage(chat_id=chat_id, text=msg)

        send("Hey! The price of Bitcoin is {}€ now that's out of our limits".format(finalprice), "-1001566083560")

while True:
    sleep(2)
    Telechat()