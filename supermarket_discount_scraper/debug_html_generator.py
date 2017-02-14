import time
from selenium import webdriver

url = 'http://www.wholefoodsmarket.com/sales-flyer/cupertino'
cmd = 'return document.documentElement.outerHTML'
driver = webdriver.Chrome(executable_path='./bin/chromedriver')
driver.get(url)
time.sleep(5)
html = driver.execute_script(cmd)

with open("whold_food_debug_html.txt", 'w+') as fout:
    fout.write(html)