#for loop
name="mamatha"
for i in name:
    print(i)
# and 
list=["hxychh",78,90.0,"sgdhcxbhydh"]
for i in list:
    print(i) 


#while loop
i=0
while i<10:
    print(i)
    i=i+1

#breake statement
count=[0,1,2,3,4,5]
for i in count: 
    if i==4:
      break
    print(i)
    


#continue statement
count=[0,1,2,3,4,5,6,7,8,9]
for i in count: 
    if i==6:
      continue
    print(i)
    

# print the numbers from 1 to 10
for i in range (11):
 print(i)
 
#or  print the numbers from 1 to N
for i in range(1,n+1):
  print(i)


# sum of the numbers from 1 to 10
sum =0
for i in range(1,11):
   sum=sum+i
   print(sum)

# print the even number between 1 to 20
for i in range (2,22,2):
   print(i)

#print the odd number between 1 to 20
for i in range (1,21,2):
   print(i)

#factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

#multication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#reverse number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)


# check for prime numbers
n = int(input("Enter number: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")


# fibonacci series
n = int(input("Enter how many terms: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b


#armstrong number check
num = int(input("Enter number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10
if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

#pattern printing
n = 4
for i in range(1, n+1):
    print("* " * i)



# polindrome syndrome
num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
