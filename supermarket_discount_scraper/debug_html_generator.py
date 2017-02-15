import time
from selenium import webdriver

CONFIG_ON_SALE = 0

if CONFIG_ON_SALE == 1:  # get on sale page html source
    url = 'http://www.wholefoodsmarket.com/sales-flyer/cupertino'
else:
    url = 'http://www.wholefoodsmarket.com/sales-flyer/cupertino?qt-custom_quicktab_sales_coupons=1#qt-custom_quicktab_sales_coupons'

cmd = 'return document.documentElement.outerHTML'
driver = webdriver.Chrome(executable_path='./bin/chromedriver')
driver.get(url)
time.sleep(5)
html = driver.execute_script(cmd)

if CONFIG_ON_SALE == 1:
    with open("whold_food_debug_html.txt", 'w+') as fout:
        fout.write(html)
else:
    with open("whold_food_coupon_debug_html.txt", 'w+') as fout:
        fout.write(html)
