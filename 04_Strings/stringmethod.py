#strings are immutable
a = "Harry!! !!!!!!!!!! Prachi"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #strip the trailing characters
str1="!!!HEY"
print(str1.lstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogheading = "introduction to js"
print(blogheading.capitalize())

str1="Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))
str1="He's name is Dan. He is an honest man"
print(str1.find("is"))
str1="Welcome3"
print(str1.isalnum())
str1="Welcome"
print(str1.isalpha())
str1="hello world"
print(str1.islower())
str1="We wish u a merry christmas"
print(str1.isprintable())
str1="We wish u a merry christmas\n"
print(str1.isprintable())
str1="    "
print(str1.isspace())
str1="Prachi Loves Shivansh"
print(str1.istitle())
str1="I HATE MYSELF"
print(str1.isupper())
str1="Python is a interpreted language"
print(str1.startswith("Python"))
str1="Python Is A Interpreted Language"
print(str1.swapcase())
str1="We wish u a merry christmas"
print(str1.title())
