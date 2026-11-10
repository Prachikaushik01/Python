#python string ko sirf chipka deta ha
#explicit typeCasting:We have to do conversion by ourselves
a = "1" #here python doesnt know that 1 is a number he only knows that it is a string
b = "2"
print(a+b)
e="1"
f="2"
print(int(e)+int(f))

#Implicit typeCasting:Python do the conversion by itself
c = 1.9
d = 2
print(c+d)
'''Here python converts a smaller datatypes to a 
higher data type to prevent data loss'''

