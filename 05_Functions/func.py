#User defined functions:
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
       print("First number is greater")
    else:
     print("Second number is greater or equal")

a=9
b=8
calculateGmean(a,b)
isGreater(a,b)
c=8
d=7
calculateGmean(c,d)
isGreater(c,d)