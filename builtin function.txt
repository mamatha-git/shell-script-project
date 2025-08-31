# string cocatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) 


#string inbuilt function
# length of the string
a= "Python is awesome"
b=len(a) 
print(b) 
#or
a= "Python is awesome"
print(len(a))
      

# upperacse
text = "Python is awesome"
uppercase=(text.upper())
print("Uppercase:",uppercase)
#Or
text = "Python is awesome"
print(text.upper())


#lowercase
text = "Python is awesome"
lowercase=(text.lower())
print("Lowercase:",lowercase)
#Or
text = "Python is awesome"
print(text.lower())
    

#replace
text="Python is awesome"
newname=text.replace("awesome","easy")
print("modified:",newname)


#split
text = "Python is awesome"
new = text.split()
print("Words:",new)
#or
text = "Python is awesome"
print(text.split())


#strip(to remove the extra space)
text = "python is awesome   "
stripped_text = text.strip()
print("new:", stripped_text)
#or
text = "python is awesome   "
print(text.strip())


# in ( to check it is there  or not)
text = "mamatha"
word="w"
if word in text:
    print("yes")
else:
    print("no data found")

# integers
num1=19
num2=13
result=num1+num2
print(result)

#float
num1=19.7
num2=13.6
result=num1+num2
print(result)