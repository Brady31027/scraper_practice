from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

print("-- get green span --")
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs4 = BeautifulSoup(html.read(), "html.parser")
l_name = bs4.findAll("span", {"class":"green"})
for name in l_name:
	print(name.get_text())

print("-- get h tag --")
l_h_tag_target = ["h1", "h2", "h3", "h4", "h5", "h6"]
l_h_tag = bs4.findAll(l_h_tag_target)
for h_tag in l_h_tag:
	print (h_tag)

print("-- get green and red span --")
l_green_red_target = ["green", "red"]
l_green_red = bs4.findAll("span", l_green_red_target)
for green_red in l_green_red:
	print(green_red.get_text())

print("-- get text equal to the prince --")
l_name = bs4.findAll(text="the prince")
print(len(l_name))

print("-- get keyword text --")
l_kw = bs4.findAll(id='text')
print(l_kw[0].get_text())