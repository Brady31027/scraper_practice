from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

class WholeFoodStoreLocator():
    wholefood_url = 'http://www.wholefoodsmarket.com/sales-flyer'
    l_states = [ 'Alabama', 'Arizona', 'Arkansas', 'California',
                  'Colorado', 'Connecticut', 'District Of Columbia',
                  'Florida', 'Georgia', 'Hawaii', 'Idaho',
                  'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                  'Louisiana', 'Maine', 'Maryland', 'Massachusetts']
    l_stores = []

    def get_stores(self):
        return self.l_stores

    def fetch_store_online(self):
        # use Google chrome to debug
        # driver = webdriver.Chrome(executable_path='./bin/chromedriver')
        driver = webdriver.PhantomJS(executable_path='./bin/phantomjs')
        driver.get(self.wholefood_url)
        # wait for page loading, try to use implicit waiting
        time.sleep(3)
        #with open('wholefood_us_data.txt', 'w') as fout:
        for state in self.l_states:
            select = Select(driver.find_element_by_id('edit-state'))
            select.select_by_visible_text(state)
            time.sleep(0.5)  # sleep 0.5 second to wait for the store list loaded
            select = Select(driver.find_element_by_id('edit-store'))
            store_options = select.options
            for index in range(1, len(store_options)):
                self.l_stores.append( {state: store_options[index].text} ) # save as dict
        driver.close()
        driver.quit()

    def dump_stores_as_stdout(self):
        for iter in self.l_stores:
            print(iter)

    def dump_stores_as_text(self):
        with open("wholefood_us_data.txt","w+") as fout:
            for iter in self.l_stores:
                for state, store in iter.items():
                    try:
                        fout.write(state+" : "+store+"\n")
                    except IOError as e:
                        print("error occurs during text data dump:" + e)
                        pass

    def dump_store_as_csv(self):
        with open("wholefood_us_data.csv", "w+") as csvout:
            csv_writer = csv.writer(csvout)
            csv_writer.writerow(['state', 'store']) #title
            for iter in self.l_stores:
                for state, store in iter.items():
                    try:
                        csv_writer.writerow([state, store])
                    except IOError as e:
                        print("error occurs during csv data dump:" + e)
                        pass