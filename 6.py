from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find("table", {"id":"giftList"}).tr.next_siblings:
	print(sibling)