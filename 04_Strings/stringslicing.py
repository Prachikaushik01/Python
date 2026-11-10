names = "Harry,Shubham"
print(names[0:5]) #if we want to print only harry then write first letter index no and then last one which we want
'''0:4 means index 0 se start karo index 4 se pehle stop karo n-1 index tak jaata hai python'''
print(len(names))
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
#for function we use parenthesis but for slicing we use square brackets
#Negative slicing:
print(fruit[0:-3])
#-3 kese execute hota hai length of string-3 hoga 2 bacha to pehle ki 2 string print hojayegi like pront(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) #isme kuch nhi print nahi hoga to python yaha pr length interprter lgayega to 4:2 hojayega pr iska kuxh sense nahi h chhote se bada hona chye bde se chota nahi
'''Quick quiz:
nm="Harry" 
print(nm[-4:-2])
5-4=1
5-2=3
ar will be printed'''