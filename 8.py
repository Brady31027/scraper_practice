from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://www.pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")

images = bs.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img[1-9]\.jpg")})
for img in images:
	print(img)