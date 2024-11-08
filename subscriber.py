from datetime import datetime

class Subscriber:
    c = 0
    def __init__(self,FRname,FMname,age,height,weight,price):
        self.__FRname = FRname 
        self.__FMname = FMname 
        self.__age = age 
        Subscriber.c += 1 
        self.__code = Subscriber.c
        self.__height = height 
        self.__weight = weight
        self.__price = price
        self.__subscriptionDate = datetime.now()
        
    
    @property
    def FRname(self):
        return self.__FRname
    
    @FRname.setter
    def FRname(self,value):
        if len(value) >= 3:
             self.__FRname = value
         
        
        
    @property
    def FMname(self):
        return self.__FMname
    
    @FMname.setter
    def FMname(self,value):
        if len(value) >= 3:
             self.__FMname = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value >= 15:
             self.__age = value
             
             
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,value):
        self.__code = value
    
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,value):
        self.__weight = value
             
    
    @property
    def price(self):
        return self.__price  
    @price.setter
    def price(self,value):
        if 200 <= value:
             self.__price = value
          
    
     
    @property
    def subscriptionDate(self):
        return self.__subscriptionDate    
        
    def display(self):
        return f"First name        : {self.__FRname}\nFamily name       : {self.__FMname}\nAge               : {self.__age}\nCode              : {self.__code}\nHeight            : {self.__height}cm\nWeight            : {self.__weight}Kg\nprice             : {self.__price}$\nSubscription date : {self.__subscriptionDate}"