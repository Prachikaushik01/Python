temp=int(input("Enter Your Temperature: "))
if(temp<10):
    print("It's Very Cold!Wear Warm clothes.")
elif(10<=temp<=20):
    print("It's Cold.You May Need A Jacket")
elif(21<=temp<=30):
    print("The Weather is pleasant")
elif(31<=temp<=40):
    print("Its Hot!Stay hydrated")
else:
    print("Its Extremely hot!Stay Indoor if possible")