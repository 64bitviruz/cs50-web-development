# defining a list of name 
list = ['manish ' , 'hari ','prince', 'min']

print(list[0])
list.append('thomas')# this is a way of adding name in the list 

list.sort()#this line of code puts the in alphabetical order

print(list)

#in terms of creating a set 
## set - collection of unique values 
print ('------------------------------------------------')
s = set()# in a set you  cannot repeat the same number
#adding elements in set 
s.add(1)
s.add(2)
s.add(3)
s.add(4)# adding number in the set 
s.add(5)

s.remove(3)# removes the number of the set

print(s)
print(f"there are {len(s)} numbers in a the set ")# len provides us the number of numbers in  a set