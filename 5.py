from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs4 = BeautifulSoup(html, "html.parser")

for child in bs4.find("table", {"id":"giftList"}).children:
	print(child)