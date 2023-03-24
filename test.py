# create a bus booking program
# need ,total seats ,open seats ,total passangers,capaxity of indicator
class Bus: #1 creating a class 
    def __init__(self,capacity): #2  defing the capacity in class
        self.capacity = capacity #3  this stores that capacity 
        self.passangers = []     #4  declaring a empty list for storing passangers
    def add_passanger(self,name):# 6 way of adding Passanger in the list
        if not self.open_seats():
            return False
            
        self.passangers.append(name)# adding passanger with the name 
        return True

    def open_seats(self): #declelaring a variable for open seats
        return self.capacity - len(self.passangers)    
buses = Bus(5)                   #5  creating a  variable for storing the number of capacity that a bus can hold

# adding people in bus now 
for i in range (5):
    if i < 5:
        people = input("enter names: ").strip()
for person in people:
    success = buses.add_passanger(person) # declaring a variable which adds people in bus
    if success:
        print(f"we added {person} to the bus sucessfullly")
    else:
        print(f"{person} was not added to the bus deu to capacity")


