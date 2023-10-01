def Fixed_discount(Amount : float , discount : float):
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
        return Amount - (iter * discount)
    except:
        iter = float(Amount/1)
        print('inprocess')
        print(iter)
        print(iter * discount)
        return Amount - iter