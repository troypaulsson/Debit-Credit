

from requests import get
from sys import argv
import numpy as np
import pandas as pd
import time

cards = pd.read_excel('testCards.xlsx')
counter = 0

def _check_(cc):
	p =b= None
	r 	= get(f"https://lookup.binlist.net/{cc}",
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		"Accept-Version": "3"}).json()
	cards['Type'][counter] = r["type"]
	print(cards)

if __name__ == '__main__':
	while counter <= len(cards)-1:
		cc = str(cards['Credit_Card_Number'][counter])
		_check_(cc)
		counter +=1
		time.sleep(6)

file_name = 'testCardsOutput.xlsx'
cards.to_excel(file_name)
