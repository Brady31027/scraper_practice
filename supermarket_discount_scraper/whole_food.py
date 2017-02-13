from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

g_l_state = [ 'Alabama', 'Arizona', 'Arkansas', 'California',
              'Colorado', 'Connecticut', 'District Of Columbia',
              'Florida', 'Georgia', 'Hawaii', 'Idaho',
              'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
              'Louisiana', 'Maine', 'Maryland', 'Massachusetts']

wholefood_url = 'http://www.wholefoodsmarket.com/sales-flyer'

# use Google chrome to debug
#driver = webdriver.Chrome(executable_path='./bin/chromedriver')
driver = webdriver.PhantomJS(executable_path='./bin/phantomjs')
driver.get(wholefood_url)

# wait for page loading, try to use implicit waiting
time.sleep(3)

fout = open('wholefood_us_data.txt', 'w')

for state in g_l_state:
    select = Select(driver.find_element_by_id('edit-state'))
    select.select_by_visible_text(state)
    try:
        fout.write("===== state : "+ state + " =====\n")
        time.sleep(0.5)  # sleep 0.5 second to wait for the store list loaded
        select = Select(driver.find_element_by_id('edit-store'))
        store_options = select.options
        for index in range(1, len(store_options)):
            fout.write("store: " + store_options[index].text + "\n")
    except IOError as e:
        pass

fout.close()
driver.close()
driver.quit()