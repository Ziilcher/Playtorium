from module.DiscountModule import DiscountModule
import json

def search_item(name):
    for item in stock:
        if name.lower() == item['name'].lower():
            return item
        
def search_campaign(name):
    for campaign in campaigns:
        if name.lower() == campaign['name'].lower():
            return campaign

with open('src/stock.json') as f:
    stock = json.load(f) 

with open('src/campaign.json') as f:
    campaigns = json.load(f) 


while True:
    discount_module = DiscountModule()
    while True :
        cart_input = input('Enter product (c to confirm) : ')
        if search_item(cart_input) != None:
            try :
                quantity_input = int(input('Enter quantity : '))
                if quantity_input > 0:
                    discount_module.add_item_to_cart(search_item(cart_input))
                    discount_module.add_quantity(quantity_input)
                
            except ValueError: print('Please fill the correct number.')
        elif cart_input == 'c':
            break
        else : print("this product doesn't exist in the stock.")
        
    while True :
        coupon_campaign_input = int(input('coupon campaign : 1 | Fixed amount || 2 | Percentage discount || 3 | Skip : '))
        if coupon_campaign_input == 1 :
            coupon_campaign = 'Fixed Amount'
            discount_module.add_campaign(search_campaign(coupon_campaign))
            break
        elif coupon_campaign_input == 2 :
            coupon_campaign = 'Percentage discount'
            discount_module.add_campaign(search_campaign(coupon_campaign))
            break
        elif coupon_campaign_input == 3 :
            break
        
        else : print("Dosen't has this campaign.")
        
    while True :   
        ontop_campaign_input = int(input('coupon campaign : 1 | Percentage Discount by Item Category || 2 | Discount by points || 3 | Skip : '))
        if ontop_campaign_input == 1 :
            ontop_campaign = 'Percentage Discount by Item Category'
            discount_module.add_campaign(search_campaign(ontop_campaign))
            break
        elif ontop_campaign_input == 2 :
            ontop_campaign = 'Discount by points'
            discount_module.add_campaign(search_campaign(ontop_campaign))
            break
        elif ontop_campaign_input == 3 :
            break
        
        else : print("Dosen't has this campaign.")
        
    while True :   
        seasonal_campaign_input = int(input('coupon campaign : 1 | Special campaign || 2 | Skip : '))
        if seasonal_campaign_input == 1 :
            seasonal_campaign = 'Special campaign'
            discount_module.add_campaign(search_campaign(seasonal_campaign))
            break
        elif seasonal_campaign_input == 2 :
            break
        
        else : print("Dosen't has this campaign.")
        
    total_price = discount_module.apply_discounts()
    print(total_price)
            
        
        
    
    
        

