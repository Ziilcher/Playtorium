def Fixed_discount(Amount, discount):
    return Amount - discount

def Percentage_discount(Amount, percentage):
    if percentage > 100 :
        percentage = 100
    else : 
        percentage
    
    return Amount * ((100 - percentage)/100)

def Percentage_discount_category(Amount, category, per_discount):
    if category == "Clothing" :
        return Amount * ((100 - per_discount)/100)
    else : 
        return Amount

def Discount_points(Amount, customer_points):
    capped = Amount * 0.2
    if customer_points <= capped:
        return Amount - customer_points
    else :
        return Amount - capped
    
def Special_campaigns(Amount, every, discount):
    try:
        iter = int(Amount/every)
    except:
        iter = int(Amount/1)
    
    return Amount - (iter * discount)