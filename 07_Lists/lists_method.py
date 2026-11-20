l = [11,45,1,2,4,6]
print(l)
l.append(7) #7 get added to the list now
print(l)
l.sort() #gets arrange in numberwise in ascneding order
print(l)
l.sort(reverse=True) #gets arrange in descending order
print(l)
l.reverse() #jo original list h usse ulta kar deta h
print(l)
print(l.index(1)) #1 no ki inex mil jayegi jo ki 2 h
#Jab method list modify karta hai Inhe separately likh sakte ho eg append
#Jab method koi value return karta hai Inka result dekhne ke liye print() lagana padega.
print(l.count(1)) #count karega ki 1 kitni baar arha h
m = l.copy()
m[0] = 0
print(m)
l.insert(1,899) #1st inedex pr 899 ko insert krna chahte h
print(l)
p = [900,1200,2200]
l.extend(p) #p ko kholo aur l ke end mei rkhdo
print(l)
#Concanecating the lists
k = l + p
print(k)
#Lists are mutable ie change kar sakte hai