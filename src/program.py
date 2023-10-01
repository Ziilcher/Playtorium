from module.discount import *
import json

with open('src/stock.json') as f:
    stock = json.load(f)

stock_name = []
item_price = dict()
item_catagory = dict()

for item in stock:
    name = item['name']
    stock_name.append(name)
    price = item['price']
    category = item['category']
    item_price[name] = price
    item_catagory[name] = category

while True:
    cart = []
    quantities = []
    categories = []
    Discount_price = 0
    total_price = 0
    while True:
        item_name = input('Enter the product you want to buy (c to Confirm): ')   
        if item_name in stock_name:
            try:
                item_quantities = int(input('Enter the quantities you want to buy : '))
                if item_quantities >= 0:
                    quantities.append(item_quantities)
                    cart.append(item_name)
                    categories.append(item_catagory[item_name])
                else: print('Invalid')
                
            except ValueError:
                print("Please fill the number")
                
                
        elif item_name == 'c':
            break
        else: print("Dosen't has this product in the stock.")
                
    while True:            
        try:
            coupon_input = int(input('1 : Fixed amount | 2 : Percentage discount | 3 : Skip : '))
            if coupon_input == 1 or coupon_input == 2 or coupon_input == 3:
                break
            else: print("Doesn't has this campaign.")
        except ValueError:
            print("Doesn't has this campaign.")
            
    while True:        
        try:
            OnTop_input = int(input('1 : Percentage discount by category | 2 : Discount by point | 3 : Skip : '))
            if OnTop_input == 1 or OnTop_input == 2 or OnTop_input == 3:
                break
            else: print("Doesn't has this campaign.")
        except ValueError:
            print("Doesn't has this campaign.")
            
    for item, quantity, category in zip(cart, quantities, categories):
        total_price += (float(item_price[item]) * int(quantity))
        if OnTop_input == 1:
            Discount_price += Percentage_discount_category((float(item_price[item]) * int(quantity)), category, 15)
        else :    
            Discount_price += (float(item_price[item]) * int(quantity))
            
    #coupon    
    if coupon_input == 1:
        Discount_price = Fixed_discount(Discount_price, 50)
    elif coupon_input == 2:
        Discount_price = Percentage_discount(Discount_price, 15)
    elif coupon_input == 3:
        pass
        
    #on top
    if OnTop_input == 2:
        Discount_price = Discount_points(Discount_price, 68)
    elif OnTop_input == 3:
        pass
        
    #seasonal
    Discount_price = Special_campaigns(Discount_price, 300, 40)

    print('item : ', cart)
    print('quantity : ', quantities)
    print('Total price : ' ,str(total_price) + " Baht")    
    print('Discount price : ' ,str(Discount_price) + " Baht")
    