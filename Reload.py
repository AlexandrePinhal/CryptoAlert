from time import *

#while True:
    sleep(2)
    print("salut")



from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from time import sleep
from request import *
import re
import json

page = requests.get("https://www.gofundme.com/f/eric-stevens-care-trust")
soup = BeautifulSoup(page.text, 'lxml')
Amount_raised = soup.find_all('h2', class_='m-progress-meter-heading')[0].get_text()

print(Amount_raised)