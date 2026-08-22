# 13. Hospital Management — Aggregation + Inheritance
# Create:
# Person
# ├── Doctor
# └── Patient
# and an Address class.
# • Doctor and Patient should inherit from Person.
# • Both should contain an Address object.
# • Add different attributes for Doctor and Patient.
# • Override display() in both child classes.
# • Use super() where required.
# This combines inheritance + aggregation + overriding.

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def display(self):
        print("Name : ",self.name)
        print("Age : ", self.age)
        
        
class Doctor(Person):
    def __init__(self, name, age,specialization,address):
        super().__init__(name, age)
        self.specialization = specialization
        self.address = address
        
    def display(self):
        super().display()
        print("Specialization : ",self.specialization)
        print("City : ",self.address.city)
        print("pincode : ",self.address.pincode)
 
class Patient(Person):
    def __init__(self, name, age,disease,address):
        super().__init__(name, age)
        self.disease = disease
        self.address = address
    
    def display(self):
        super().display()
        print("Disease is ",self.disease)
        print("City : ",self.address.city)
        print("pincode : ",self.address.pincode)
        
class Address:
    def __init__(self,city,pincode):
        self.city = city
        self.pincode = pincode
   
add1 = Address("Pune",411045)
add2 = Address("Mumbai",311033)

doc1 = Doctor("Dr.Gaurav",26,"Cardiac",add1) 
doc1.display()
pt1 = Patient("Sarthak",22,"Fever",add2)
pt1.display()