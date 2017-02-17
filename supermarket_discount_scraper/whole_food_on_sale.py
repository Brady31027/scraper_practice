import re
import requests
from bs4 import BeautifulSoup

g_DEBUG = False
g_debug_html = """
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">Country Natural Beef</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">Boneless Rib-Eye Steak</div></div>
<div class="views-field views-field-body"><div class="field-content">Valentine's Day special. From cattle raised with no added hormones and no antibiotics ever.</div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="sales-flyer-image"><img src="//assets.wholefoodsmarket.com/sale_items/249409.jpg" alt=""></div><div class="prices-text"><div class="sale_line">$11.99 LB</div>
<div class="reg_line">REG $16.99-$17.99 LB / lb</div></div>
<div class="you_save">SAVE $5-$6 LB</div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
<div class="savings">SAVE $5-$6 LB
</div></span></div></div>
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">Wild · Previously Frozen</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">Lobster Tails</div></div>
<div class="views-field views-field-body"><div class="field-content">(4-5 oz) Split and broil; serve with butter for a succulent meal in minutes. Excludes cooked.</div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="sales-flyer-image"><img src="//assets.wholefoodsmarket.com/sale_items/249408.jpg" alt=""></div><div class="prices-text"><div class="sale_line">$5.99 EA</div>
<div class="reg_line">REG $9.99 EA each</div></div>
<div class="you_save">SAVE $4 EA</div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
<div class="savings">SAVE $4 EA
</div></span></div></div>
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">H&amp;G</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">Napa Valley Red Wine Blend</div></div>
<div class="views-field views-field-body"><div class="field-content">(750 ml) Dense dark fruit flavors with a deep overlay of mocha and vanilla oak.</div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="prices-text"><div class="sale_line">$14.99 EA</div>
<div class="reg_line">REG $19.99 EA each</div></div>
<div class="you_save">SAVE $5 EA</div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
<div class="savings">SAVE $5 EA
</div></span></div></div>
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">Lake Champlain Chocolates</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">Valentine's Day Chocolates</div></div>
<div class="views-field views-field-body"><div class="field-content">( 0.4 - 12 oz )</div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="prices-text"><div class="sale_line">20% OFF</div>
<div class="reg_line">REG $1.19-$39.99 EA each</div></div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
</span></div></div>
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">Responsibly Grown</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">20-Stem Tulips</div></div>
<div class="views-field views-field-body"><div class="field-content"></div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="sales-flyer-image"><img src="//assets.wholefoodsmarket.com/sale_items/249412.jpg" alt=""></div><div class="prices-text"><div class="sale_line">$15 EA</div>
<div class="reg_line">REG $17 EA each</div></div>
<div class="you_save">SAVE $2 EA</div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
<div class="savings">SAVE $2 EA
</div></span></div></div>
<div class="views-row views-row-odd">
<div class="views-field views-field-field-flyer-brand-name"><div class="field-content">Whole Foods Market®</div></div>
<div class="views-field views-field-field-flyer-product-name"><div class="field-content">Sweetheart Cake</div></div>
<div class="views-field views-field-body"><div class="field-content">( 19 oz )</div></div>
<div class="views-field views-field-nothing"><span class="field-content views-field-php-1"><div class="prices clearfix">
<div class="prices-text"><div class="sale_line">$10.99 EA</div>
<div class="reg_line">REG $14.99 EA each</div></div>
<div class="you_save">SAVE $4 EA</div>
</div><!-- prices-text --><div class="views-field views-field-field-flyer-end-date"><span class="views-label views-label-field-flyer-end-date">Valid </span><span class="date-display-single">2/8</span> - <span class="date-display-single">2/14</span></div>
<div class="savings">SAVE $4 EA
</div></span></div></div>
"""

class WholeFoodOnSale():

    on_sale_base_url = 'http://www.wholefoodsmarket.com/sales-flyer/'
    state = ''
    store = ''
    prod_brand_class_identifier = 'views-field views-field-field-flyer-brand-name'
    prod_name_class_identifier = 'views-field views-field-field-flyer-product-name'
    prod_desc_class_identifier = 'views-field views-field-body'
    prod_image_img_identifier = 'img'
    onsale_price_class_identifier = 'sale_line'
    original_price_class_identifier = 'reg_line'
    save_money_price_class_identifier = 'you_save'
    valid_date_span_identifier = 'date-display-single'

    def __init__(self, state, store):
        self.state = state
        self.store = store

    def get_state(self):
        return self.state

    def get_store(self):
        return self.store

    def generate_url(self, raw_store):
        #print("original store name = " + raw_store)
        refined_store = re.sub("\s+", '', raw_store)
        refined_store = refined_store.lower()
        #print("refined store name = " + refined_store)
        return self.on_sale_base_url+refined_store

    def connect_to_server(self, url):
        print("connect to "+url)
        r =requests.get(url)
        print("http request return code : "+ str(r.status_code)) # should be 200
        if r.status_code != 200:
            print("connection error, return code is not 200")
            return None
        bs_obj = BeautifulSoup(r.text, "html.parser")
        return bs_obj

    def get_product_brand(self, prod_html):
        try:
            brand_name = prod_html.find("div", { "class" : self.prod_brand_class_identifier })
            brand_name = brand_name.get_text()
        except:
            print("Cannot find product brand")
            return 'NULL'
        return brand_name

    def get_product_name(self, prod_html):
        try:
            prod_name = prod_html.find("div", { "class" : self.prod_name_class_identifier })
            prod_name = prod_name.get_text()
        except:
            print("Cannot find product name")
            return 'NULL'
        return prod_name

    def get_product_desc(self, prod_html):
        try:
            prod_desc = prod_html.find("div", {"class": self.prod_desc_class_identifier})
            prod_desc = prod_desc.get_text()
        except:
            print("Cannot find product desc")
            return 'NULL'
        else:
            return prod_desc

    def get_onsale_price(self, prod_html):
        try:
            onsale_price = prod_html.find("div", {"class": self.onsale_price_class_identifier})
            onsale_price = onsale_price.get_text()
        except:
            print("Cannot find onsale price")
            return 'NULL'
        else:
            return onsale_price

    def get_original_price(self, prod_html):
        try:
            original_price = prod_html.find("div", {"class": self.original_price_class_identifier})
            original_price = original_price.get_text()
        except:
            print("Cannot find original price")
            return 'NULL'
        return original_price

    def get_discount_delta(self, prod_html):
        try:
            discount_delta = prod_html.find("div", {"class": self.save_money_price_class_identifier})
            discount_delta = discount_delta.get_text()
        except:
            print("Cannot find discount delta")
            return 'NULL'
        return discount_delta

    def get_valid_date(self, prod_html):
        try:
            l_valid_date = prod_html.findAll("span", {"class": self.valid_date_span_identifier})
            if len(l_valid_date) != 2:
                print("valid date data number is incorrect")
                return "NULL"
        except:
            print("valid date data number is incorrect")
            return "NULL"
        date = "Valid from {} to {}".format(l_valid_date[0].get_text(), l_valid_date[1].get_text())
        return date

    def get_prod_img(self, prod_html):
        try:
            prod_img = prod_html.find("img")['src']
        except:
            print("No prod image")
            return 'NULL'
        return ('http:' + prod_img)

    def get_on_sale_item(self):
        if g_DEBUG is True:
            bs_obj = BeautifulSoup(g_debug_html, "html.parser")
        else:
            raw_store = self.get_store()
            url = self.generate_url(raw_store)
            bs_obj = self.connect_to_server(url)
            if not bs_obj: # connect to server return none, connection error!
                print("unable to parse by bs4 because of connection error")
                return []
        l_on_sale_items = bs_obj.findAll("div", { "class" : "views-row views-row-odd" })
        print("On sale product count = " + str(len(l_on_sale_items)))
        for product in l_on_sale_items:
            print("------------------------------\n")
            print(self.get_product_brand(product))
            print(self.get_product_name(product))
            print(self.get_product_desc(product))
            print(self.get_prod_img(product))
            print(self.get_onsale_price(product))
            print(self.get_original_price(product))
            print(self.get_discount_delta(product))
            print(self.get_valid_date(product))

onSaleObj = WholeFoodOnSale("California", "Cupertino")
onSaleObj.get_on_sale_item()

