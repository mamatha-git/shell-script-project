#variable declaration
my_varible=50
print(my_varible)



#types of varible
#global varible
y=18
def my_function():
     print(y)

my_function()
print(y)  


#local varible
def mamatha():
     t=7
     print(t)

mamatha()
print(t) # shows it is not defined means  it is local scope varible not access for outside the function
