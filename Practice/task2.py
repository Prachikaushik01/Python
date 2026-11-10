'''Create a python program capable of greeeting 
you with good morning,good afternoon and good evening
Your program should use time module to get the 
current hour'''
'''Good Morning: 12:00 AM to 11:59 AM (Midnight to Noon)
Good Afternoon: 12:00 PM to 4:59 PM (Noon to Evening)
Good Evening: 5:00 PM to 11:59 PM (Evening to Midnight)'''
import time
current_hour = int(time.strftime('%H'))
if(0<=current_hour<12):
    greeting="Good Morning"
elif(12<=current_hour<17):
    greeting="Good Afternoon"
else:
    greeting="Good Evening"
current_time=time.strftime("%I:%M %p")
print("Current Time:", current_time)
print(greeting)
'''%H-24 HOUR FORMAT(00-23)
   %I-12 HOUR FORMAT(01-12)
   %M-MINUTES(00-59)
   %p-AM/PM'''