import re


class WholeFoodOnSale():
    on_sale_base_url = 'http://www.wholefoodsmarket.com/sales-flyer/'
    state = ''
    store = ''

    def __init__(self, state, store):
        self.state = state
        self.store = store

    def get_state(self):
        return self.state

    def get_store(self):
        return self.store

    def generate_url(self, raw_store):
        print(raw_store)
        refined_store = re.sub("\s+", '', raw_store)
        refined_store = refined_store.lower()
        print(refined_store)
        return self.on_sale_base_url+refined_store

    def get_on_sale_item(self):
        pass

"""
onSaleObj = WholeFoodOnSale("California", "Del Mar")
store = onSaleObj.get_store()
url = onSaleObj.generate_url(store)
print(url)
"""
