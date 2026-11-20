'''Create a python program capable of greeeting 
you with good morning,good afternoon and good evening
Your program should use time module to get the 
current hour'''
'''Good Morning: 12:00 AM to 11:59 AM (Midnight to Noon)
Good Afternoon: 12:00 PM to 4:59 PM (Noon to Evening)
Good Evening: 5:00 PM to 11:59 PM (Evening to Midnight)'''
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17 ):
    print("Good Afternoon Sir")
elif(hour>=17 and hour<0):
    print("Good Night Sir")

                                       