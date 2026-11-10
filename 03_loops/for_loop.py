name='Abhishek'
for i in name:
    print(i)
    if(i=="b"):
        print("This is something special!")

colors=["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
     print(i)

#for k in range(5):it runs from 0 to n-1
   #print(k)
#for k in range(5):
   #print(k+1)
#for k in range(1,9): it runs from 1 to n-1
   #print(k)
for k in range(1,7,5):
   print(k)
   '''step argument in loops it increases by last no and increase upto the range it have 
   in suppose 1,12,3 so it will print 1,4,7,10 and it will stop here and not print 13 as the range is till 12 only'''