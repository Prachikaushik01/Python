tup = (1,5,6,7,8,66)
print(type(tup), tup) #isme class tup aayega pr jese hi ek element hojayega class int hojayega 
#Agr ek element ka tupple banana h toh uske bd comma daalna padega tabhi wo tupple consider hoga
#Tuples are unchangeable
#Why we use tuples=when we want to create a constant which caanot be change by mistake
#Can store diff datatypes
print(tup[0])
print(tup[1])

if 342 in tup:
    print("Yes 342 is present")
    tup2= tup[1:4]
    #List aur tuple mei ky diff h diff bs itna h ki list ko change kr sktr h pr tuple ko nhi change krskte