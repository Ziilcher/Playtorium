class DiscountModule:
    def __init__(self):
        self.cart = []
        self.quantities = []
        self.discount_campaigns = []
    
    def add_item_to_cart(self, item):
        self.cart.append(item)
        
    def add_quantity(self, quantity):
        self.quantities.append(quantity)
        
    def add_campaign(self, campaign):
        self.discount_campaigns.append(campaign)
        
    def apply_discounts(self):
        total_price = 0
        print(self.cart)
        print(self.discount_campaigns)
        
        for item, quantity in zip(self.cart, self.quantities):
            item_price = item['price'] * quantity
            total_price += item_price
            
        for campaign in self.discount_campaigns :
            if  campaign['name'] == 'Fixed Amount' :
                total_price -= float(campaign['Amount'])
            elif campaign['name'] == 'Percentage discount' :
                total_price -= float(total_price * (campaign['Percentage']/100))
            elif campaign['name'] == 'Percentage Discount by Item Category' :
                category_price = 0
                for item, quantity in zip(self.cart, self.quantities):
                    if item['category'] == campaign['category']:
                        category_price += item['price'] * quantity
                total_price -= float(category_price * (campaign['Amount'] / 100))
            elif campaign['name'] == 'Discount by points':
                max_dicount = total_price * 0.2
                discount_amount = min(max_dicount, campaign['customer_points'])
                total_price -= float(discount_amount)
            elif campaign['name'] == 'Special campaign' :
                total_price -= float((total_price // campaign['every_x_baht']) * campaign['discount'])
            elif campaign['name'] == 'skip' :
                pass
        
        return max(0, total_price)