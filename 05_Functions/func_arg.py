#default arguments:
def average(a=9, b=1):
 print("The average is ", (a+b)/2)
#average(1,5)
average(5) #b ki value ye apne aap lelega

#keywords arguments:We pass values to a function by using parameter names instead of depending on their position.
average(b=9,a=21)

#Required arguments:
def average(a,b,c=1):
 print("The average is ", (a+b+c)/2)
average(5,6)

#Variable length arguments
def average(*numbers):
  total = 0
  for i in numbers:
    total = total + i

    print("Average is: ", total / len(numbers))

average(5,6)

def name(**name):
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Pankaj", lname="Kaushik", fname="Prachi")

#return statement
def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  return sum/len(numbers)

c = average(5,6,7,1)
print(c)