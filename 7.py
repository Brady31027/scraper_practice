from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

cost = bs.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print(cost)