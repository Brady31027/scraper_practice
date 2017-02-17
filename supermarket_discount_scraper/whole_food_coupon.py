import re
import requests
from bs4 import BeautifulSoup

g_DEBUG = False
g_debug_html = """

<input type="submit" id="edit-form-submit" name="op" value="Print Selected" class="form-submit"></div></fieldset>
<div class="view view-coupons view-id-coupons view-display-id-block view-dom-id-57f10f000c5051455f0ad837e50d6c55">
      <div class="view-content">

      <div class="views-row views-row-1 views-row-odd views-row-first coupon-305037">
      <div class="views-field views-field-print-select">
          <span class="field-content">
              <div class="form-item form-type-checkbox">
              <input name="print_select[0]" value="5631936" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-0">
              <label class="option" for="edit-print-select-0">Print coupon </label>
              </div>
          </span>
      </div>
      <div class="views-field views-field-field-coupon-image">
          <div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305037.png" width="120" height="150" alt="">
          </div>
      </div>
      <span class="views-field views-field-field-coupon-offer">
          <span class="field-content">$1.00 off</span>
      </span>
      <span class="views-field views-field-field-coupon-headline">
          <span class="field-content">any ONE (1) Nature’s Rancher Beef Steak New York Strip or Ribeye</span>
      </span>  </div>
<div class="views-row views-row-4 views-row-even coupon-305034">
<div class="views-field views-field-print-select">        <span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[3]" value="5631921" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-3">  <label class="option" for="edit-print-select-3">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305034.png" width="120" height="150" alt=""></div>  </div>
<span class="views-field views-field-field-coupon-offer">
<span class="field-content">$3.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any ONE (1) 60-180 tablet bottle Whole Foods Market™ Food-Cultured Multi Men's, Women's or Prenatal</span>  </span>  </div>
<div class="views-row views-row-12 views-row-even coupon-305020">
<div class="views-field views-field-print-select">        <span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[11]" value="5631881" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-11">  <label class="option" for="edit-print-select-11">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305020.png" width="120" height="150" alt=""></div>  </div>
<span class="views-field views-field-field-coupon-offer">
<span class="field-content">$1.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any TWO (2) Stonyfield Organic Single Serve 3.7-oz pouches</span>  </span>  </div>
<div class="views-row views-row-13 views-row-odd coupon-305019">
<div class="views-field views-field-print-select">        <span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[12]" value="5631876" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-12">  <label class="option" for="edit-print-select-12">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305019.png" width="120" height="150" alt=""></div>  </div>
<span class="views-field views-field-field-coupon-offer">
<span class="field-content">$1.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any TWO (2) Stonyfield Organic 5.3-oz Greek Yogurts</span>  </span>  </div>
<div class="views-row views-row-14 views-row-even coupon-305018">
<div class="views-field views-field-print-select">
<span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[13]" value="5631871" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-13">  <label class="option" for="edit-print-select-13">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305018.png" width="120" height="150" alt=""></div>  </div>
<span class="views-field views-field-field-coupon-offer">
<span class="field-content">$1.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any TWO (2) So Delicious Dairy Free Creamers ( 16 oz or larger)</span>  </span>  </div>
<div class="views-row views-row-15 views-row-odd coupon-305017">
<div class="views-field views-field-print-select">
<span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[14]" value="5631866" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-14">  <label class="option" for="edit-print-select-14">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305017.png" width="120" height="150" alt=""></div>  </div>
<span class="views-field views-field-field-coupon-offer">
<span class="field-content">$1.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any THREE (3) So Delicious Dairy Free Coconutmilk Yogurt Alternatives ( 5.6 oz or larger)</span>  </span>  </div>
<div class="views-row views-row-16 views-row-even coupon-305016">
<div class="views-field views-field-print-select">
<span class="field-content"><div class="form-item form-type-checkbox">
<input name="print_select[15]" value="5631861" class="print-checkbox form-checkbox" type="checkbox" id="edit-print-select-15">  <label class="option" for="edit-print-select-15">Print coupon </label>
</div></span>  </div>
<div class="views-field views-field-field-coupon-image">
<div class="field-content"><img typeof="foaf:Image" src="//assets.wholefoodsmarket.com/coupons/images/coupons/large/305016.png" width="120" height="150" alt=""></div>  </div><span class="views-field views-field-field-coupon-offer">        <span class="field-content">$3.00 off</span>  </span>
<span class="views-field views-field-field-coupon-headline">
<span class="field-content">any ONE (1) Renew Life Probiotic, Enzyme, Fiber or Cleanse Supplement </span> </span> </div>
"""

class WholeFoodCoupon():
    coupon_base_url = 'http://www.wholefoodsmarket.com/sales-flyer/'
    state = ''
    store = ''
    coupon_img_class_identifier = "views-field views-field-field-coupon-image"
    coupon_offer_class_identifier = "views-field views-field-field-coupon-offer"
    coupon_desc_class_identifier = "views-field views-field-field-coupon-headline"

    def __init__(self, state, store):
        self.state = state
        self.store = store

    def get_store(self):
        return self.store

    def generate_coupon_url(self, raw_store):
        refined_store = re.sub("\s+", '', raw_store)
        refined_store = refined_store.lower()
        coupon_final_url = self.coupon_base_url + refined_store + '?qt-custom_quicktab_sales_coupons=1#qt-custom_quicktab_sales_coupons'
        print("connecting to "+coupon_final_url)
        return coupon_final_url

    def connect_to_server(self, url):
        r = requests.get(url)
        print("http request return code : " + str(r.status_code))  # should be 200
        if r.status_code != 200:
            print("connection error, return code is not 200")
            return None
        bs_obj = BeautifulSoup(r.text, "html.parser")
        return bs_obj

    def get_coupon_img(self, coupon_html): #div
        try:
            img = coupon_html.find("img")['src']
        except:
            print("Cannot find coupon img")
            return 'NULL'
        return ('http:' + img)

    def get_coupon_offer(self, coupon_html): #span
        try:
            offer = coupon_html.find("span", {"class":self.coupon_offer_class_identifier})
            offer = offer.get_text()
        except:
            print("Cannot find coupon offer")
            return 'NULL'
        return offer

    def get_coupon_desc(self, coupon_html): #span
        try:
            desc = coupon_html.find("span", {"class": self.coupon_desc_class_identifier})
            desc = desc.get_text()
        except:
            print("Cannot find coupon desc")
            return 'NULL'
        return desc

    def get_coupon(self):
        if g_DEBUG == True:
            bs_obj = BeautifulSoup(g_debug_html, "html.parser")
        else:
            raw_store = self.get_store()
            url = self.generate_coupon_url(raw_store)
            bs_obj = self.connect_to_server(url)
            if not bs_obj:  # connect to server return none, connection error!
                print("unable to parse by bs4 because of connection error")
                return []
        l_coupon_html = bs_obj.findAll("div", {"class": re.compile("coupon-\d+")})
        print("Total coupon found:", len(l_coupon_html))
        for coupon in l_coupon_html:
            print("----------------------------------")
            print(couponObj.get_coupon_img(coupon))
            print(couponObj.get_coupon_offer(coupon))
            print(couponObj.get_coupon_desc(coupon))

couponObj = WholeFoodCoupon("California", "Cupertino")
couponObj.get_coupon()


