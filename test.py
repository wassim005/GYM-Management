from subscriber import Subscriber
from gym import Gym
import sys, subprocess

s1=Subscriber(FRname="Juan",FMname="Mendes",age=35,height=180.0,weight=61.0,price=250.0)
s2=Subscriber(FRname="Julio",FMname="Bernard",age=24,height=185.0,weight=75.0,price=250.0)
s3=Subscriber(FRname="Joao",FMname="Neves",age=30,height=190.0,weight=105.0,price=250.0)
s4=Subscriber(FRname="Andre",FMname="Gomes",age=18,height=175.0,weight=57.0,price=250.0)
s5=Subscriber(FRname="Ricardo",FMname="Azur",age=17,height=170.0,weight=63.0,price=250.0)
s6=Subscriber(FRname="Luciana",FMname="Gabi",age=22,height=160.0,weight=65.0,price=250.0)

g1 = Gym("Fitness", "Chicago")

g1.add(s1)
g1.add(s2)
g1.add(s3)
g1.add(s4)
g1.add(s5)
g1.add(s6)


def add():
    clear()
    print("==============================================")
    FRname = str(input("▶ Enter the first name: "))
    print("")
    FMname = str(input("▶ Enter the fammily name: "))
    print("")
    age = int(input("▶ Enter the age: "))
    print("")
    height = float(input("▶ Enter the height: "))
    print("")
    weight = float(input("▶ Enter the weight: "))
    print("")
    price = float(input("▶ Enter the price: "))
    s=Subscriber(FRname,FMname,age,height,weight,price)
    g1.add(s)
    print("==============================================")
    print("")
    print("==============================================")
    print("-----------------> Success <-----------------")
    print("==============================================")
    
    
def search():
    clear()
    code = int(input("Enter the subscriber code: "))
    print("")
    g1.search(code)
                
    
def subList():
    clear()
    g1.subList()
    
    
def totalPrice():
    clear()
    g1.totalPrice()
    
    
def remove():
    clear()
    FRname = input("Enter the subscriber's first name to remove: ")
    print("")
    g1.remove(FRname)
    
def update():
    clear()
    FRname = input("Enter the subscriber's first name to update: ")
    print("")
    g1.update(FRname)
    
    
def quitter():
    print("Merci")    

def  error():
    print("choice incorrect!!!")
def clear():
    subprocess.run('cls', shell=True)
    
d = {
    1: add,
    2: search,
    3: subList,
    4: totalPrice,
    5: remove,
    6: update,
    7: quitter
}

choice = 1

while choice != 7:
    print("""

================================================
============= Subscriber management ============
================================================
                
            1- Add a subscriber
        
            2- Search for a subscriber
        
            3- List of subscribers
        
            4- total price
        
            5- Remove a subscriber
        
            6- Update a subscriber informations
            
            7- Exit
        
          """)
    choice = int(input("Enter your choice: "))
    d.get(choice, error)()
    print("")
    input("press enter to continue......")
    clear()    