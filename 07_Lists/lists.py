marks = [3,5,6,7,8,9,10,11,12,13,14,15,16]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[-3]) #negative index:-how to convert it into positive value
print(marks[len(marks)-3]) #positive index

if "7" in marks: #why these give no bcoz when given in double inverted comma it becomes a string
    print("Yes")
else:
    print("No")
if 7 in marks: #why these give yes bcoz when not given in double inverted comma it is not a string
    print("Yes")
else:
    print("No")
#Same thing applies for string as well
if "arry" in "Harry":
    print("Yes")

print(marks[1:-1])
print(marks[0:len(marks)])
print(marks[1:5])
print(marks[1:9:3]) #first value indicate where to start from 2nd value indicate where to stop that doesnt get print and last value indicate kitne se change karna h
#list[start:end]-Start included,End excluded
#Lists Comprhension
lst = [i for i in range(4)]
print(lst)
list = [i*i for i in range(10) if i%2==0]
print(list)