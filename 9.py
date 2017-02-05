from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")

print (bs.findAll(lambda tag: len(tag.attrs) == 2))