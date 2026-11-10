a = int(input("Enter your age:\n"))
print("Your age is:", a)
'''Conditional Operators:
>,<,>=,<=,==,!='''
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
    print("You Can Drive")
else:
    print("You Cannot Drive")
'''the space after the colon and before print is 
known as indetation in python,if we dont use it
we will get an error so it is compulsory'''
num = int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is zero")
elif(num==999):
    print("Number is special")
else:
    print("Number is Positive")
print("I am Happy Now")
#Nested If Statements
num = 18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
       print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")