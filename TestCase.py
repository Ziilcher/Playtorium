import unittest
from src.module.discount import *

class testCal(unittest.TestCase):
    def test_Fixed_discount(self):
        result = Fixed_discount(600, 50)
        self.assertEqual(result, 550)
        
    def test_Percentage_discount(self):
        result = Percentage_discount(600, 10)
        self.assertEqual(result, 540)
    
    def test_Percentage_discount_catagory(self):
        amount = [350, 700, 850, 640]
        result = 0
        category = ["Clothing", "Clothing", "etc", "etc", "etc"]
        for price, cate in zip(amount, category):
            result += Percentage_discount_category(price, cate, 15)  
        self.assertEqual(result, 2382.5)

    def test_Discount_points(self):
        result = Discount_points(350+250+230, 68)
        self.assertEqual(result, 762)
        
    def test_special_campaigns(self):
        result = Special_campaigns(350+250+230, 300, 40)

if __name__ == '__main__':
    unittest.main()