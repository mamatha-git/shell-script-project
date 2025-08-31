# arithmetic operations
a=9
b=7
add=a+b
print(add) 
sub=a-b
print(sub)
mult=a*b
print(mult)
div=a/b
print(div)
floor_div=a//b
print(floor_div)
mod=a%b
print(mod)

#assignment operations
x=9
a+=7
b-=8
print(x)
print(a)
print(b)

# identity operators
x=(1,2,3)
y=(1,2,3)
result=x is y
print(result)

#or
x=(1,2,3)
y=x
result=x is not y
print(result)

#0r
x=(1,2,3)
y=(4,4,7)
result=x is y
print(result)

# logical opertors
x = True
y = False
result = x and y
print(result)# because  true and false=false
            # true and  true =true
            # false and false=false
             


#relational operations
x=5
y=8
c=x==y
d=x!=y
g=x>y
h=x<y
k=x>=y
print(c)
print(d)
print(g)
print(h)
print(k)


#membership operators
fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
print(result)
#or
name="mamatha"
word="m"
if word in name:
    print(True)

