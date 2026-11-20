countries = ("Spain","Italy","India","England","Germany")
temp= list(countries)
temp.append("Russia") #add item
temp.pop(3) #remove item
temp[2] = "Finland" #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan","Afghanisthan","Banglaesh","Bangladesh","Srilanka")
countries2= ("Vietnam","India","China")
southEastAsia= countries+countries2
print(southEastAsia)

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)
res = tuple1.index(3)
print('3 is found at index:', res)
res = tuple.index(3,4,8)
print('Again 3 is found at index:', res)
#Slicing	        Index method
#tuple[1:8:2]	tuple.index(3,4,8)
#Start	         Element
#Stop	         Start
#Step	         Stop
res = len(tuple1)
print('Length is:', res)
#Tuples are immutable ie change nahi kar sakte