from subscriber import Subscriber

class Gym:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.list = []
    
    def __str__(self):
        return f"==============================================\n==============================================\n                 name: {self.name}\n             Address: {self.address}\n==============================================\n==============================================\n\n"
        
        
    def add(self , subscriber):
        self.list.append(subscriber)
        
    def search(self , code):
        print(self)
        exist = False
        for s in self.list:
            if s.code == code:
                exist = True
                print("==============================================")
                print("==============================================")
                print(s.display())
                print("==============================================")
                print("==============================================")
        if exist == False:
            print("The subscriber cannot be found: ")
            
    def subList(self):
        print(self)
        for subscriber in self.list:
            print("==============================================")
            print(subscriber.display())
            print("==============================================")
        
        print("")
            
    def totalPrice(self):
        total = 0
        for s in self.list:
            total += s.price
        
        print("==============================================")
        print("==============================================")
        print(f"----------->  the total price is: {total} $")
        print("==============================================")
        print("==============================================")
        
    def remove(self, FRname):
        subscriber_to_remove = None
        for subscriber in self.list:
            if subscriber.FRname == FRname:
                subscriber_to_remove = subscriber
                break


        if subscriber_to_remove:
            self.list.remove(subscriber_to_remove)
            removed_code = subscriber_to_remove.code
            print(f"----> Subscriber '{FRname}' with code {removed_code} has been removed.")


            for subscriber in self.list:
                if subscriber.code > removed_code:
                    subscriber.code -= 1
        else:
            print(f"----> No subscriber found with the first name: {FRname}")
            
    def update(self, FRname):
        subscriber_to_update = None
        for subscriber in self.list:
            if subscriber.FRname == FRname:
                subscriber_to_update = subscriber
                break

        if subscriber_to_update:
            print(f"----> Updating information for subscriber '{FRname}'.")
            print("")
            print("===============================================================================")
            print("===============================================================================")
            print("")

            new_FRname = str(input(f"▶ Enter new first name (current: {subscriber_to_update.FRname}) or press Enter to keep it: "))
            if len(new_FRname) > 3:
                subscriber_to_update.FRname = new_FRname
                print("Changed successfully")
            else:
                print("----> Invalid name. Keeping the existing value.")
            print("")

            new_FMname = str(input(f"▶ Enter new family name (current: {subscriber_to_update.FMname}) or press Enter to keep it: "))
            if len(new_FMname) > 3:
                subscriber_to_update.FMname = new_FMname
                print("Changed successfully")
            else:
                print("----> Invalid name. Keeping the existing value.")
            print("")

            try:
                new_age = int(input(f"▶ Enter new age (current: {subscriber_to_update.age}) or press Enter to keep it: "))
                if new_age and new_age > 15:
                    subscriber_to_update.age = float(new_age)
                    print("Changed successfully")
                else:
                    print("----> Invalid age. Keeping the existing value.")
                print("")
                
            except ValueError:
                print("----> Invalid age. Keeping the existing value.")
                print("")

            try:
                new_height = float(input(f"▶ Enter new height (current: {subscriber_to_update.height}) or press Enter to keep it: "))
                if new_height:
                    subscriber_to_update.height = float(new_height)
                    print("Changed successfully")
            except ValueError:
                print("----> Invalid height. Keeping the existing value.")
            print("")

            try:
                new_weight = float(input(f"▶ Enter new weight (current: {subscriber_to_update.weight}) or press Enter to keep it: "))
                if new_weight:
                    subscriber_to_update.weight = float(new_weight)
                    print("Changed successfully")
            except ValueError:
                print("----> Invalid weight. Keeping the existing value.")
            print("")

            try:
                new_price = float(input(f"▶ Enter new price (current: {subscriber_to_update.price}) or press Enter to keep it: "))
                if new_price and new_price > 200:
                    subscriber_to_update.price = float(new_price)
                    print("Changed successfully")
                else:
                    print("----> Invalid price. Keeping the existing value.")
                    print("")
            except ValueError:
                print("----> Invalid price. Keeping the existing value.")
            print("")
            print("===============================================================================")
            print("===============================================================================")
            print("")
            print("---------> Subscriber information has been updated.")
            print("")
        else:
            print(f"No subscriber found with the first name: {FRname}")