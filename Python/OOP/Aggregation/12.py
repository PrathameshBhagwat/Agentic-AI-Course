# 12. E-Commerce Product — Encapsulation + Static Method
# Create a Product class.
# • Private variable __price.
# • Instance variables: name, quantity.
# • Getter/setter for price.
# • Instance method total_price().
# • Static method calculate_gst(price) that calculates GST.
# • Display the final product price including GST. 

class Product:
    gst = 0.18
    @staticmethod
    def cal_gst(amount):
        amount *= 0.18
        return amount
    
    def __init__(self,name,quantity):
        self.name = name 
        self.quantity = quantity
        self.__price = 0
        
    def get_price(self):
        return self.__price 
    
    def set_price(self,amount):
        self.__price= amount
        
    def total_price(self):
        gst=Product.cal_gst(self.__price)
        price_with_gst = self.__price + gst 
        final_amount = price_with_gst * quantity
        print("Final Product price (Including GST) : ", final_amount)




def set_price():
    amount = int(input("Enter the price of the product : "))
    pr1.set_price(amount)

product_name = input("Enter the product name : ")
quantity = int(input("Enter the quantity of the product : "))
pr1 = Product(product_name,quantity)
set_price()
pr1.total_price()