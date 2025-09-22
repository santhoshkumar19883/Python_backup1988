""" for i in range(2,100,3):
    print(i) """
""" fruits=["banana","apple","orange","cherry","papaya"]
""" """ for a in fruits:
    print(a) """
""" val= """"orange" """
for a in range(len(fruits)):
    if a == 4:
        print(f"{a} =====> {fruits[a]}")

print(fruits[2]) """
""" for i in range(0,21,2):
    print(i) """

""" total = 0
for i in range(1,101):
    total = total+i

print(total) """
#Print numbers 1 to 10 using a for loop.
""" total=5
for i in range(1,11):
    print(f"{total}*{i}={total*i}") """
""" """ """ a="santhosh" """
""" for i in a:
    print(i) """
""" b=len(str(a))
for i in b:
    print((i)) """ """ """
""" """ """ """ """ """  
#Reverse a string using a for loop.
""" a="prabhat" """
""" for i in range(len(a)-1,-1,-1):
    print(a[i]) """

""" b = ""
for i in a:
    b = i + b
print(b) """
""" a="santhosh"
b=["a","e","i","o","u"]
for i in a:
    if i in b:
        b+=1
print(b) """
#Count the number of vowels in a string using a for loop.
""" a="Prabhatue"
t=0
for i in a:
    if i in "aeiou":
        t=t+1
print(t)
 """
#Find the largest number in a list using a for loop.
""" a=[12,31,45,36,77,51,123]
t=a[0]
for i in a:
    if i > t:
        t = i
print(t) """
#Print numbers 1 to 10 using a for loop.
""" for i in range(1,11,1):
    print(i) """
#Print even numbers from 1 to 20 using a for loop.
""" for i in range(2,21,2):
    print(i) """
#Find the sum of numbers from 1 to 100 using a for loop.
"""  for i in range(1,100):
    a=0
    a=a+i
    print(a)  """
""" a="santhosh"
for i in a:
    print((i))
      """
""" s=0
a="santhosh"
for i in a:
    if i in "aeiou":
        s=s+2
print(s) """
#Print all elements of a 2D list using nested for loops
""" a=[1,2,4,5,6]
b=[6,8,9,10]
for x in a:
    for y in b:
        print(x,y)
 """
#Check if a number is prime using a for loop.
""" a = int(input("Enter a number: "))

if a <= 1:
    print(f"{a} is NOT a prime number.")
else:
    num_prime = True
    for i in range(2, int(a)):
        if a % i == 0:
            num_prime = False
            break  

    if num_prime:
        print(f"{a} is a prime number.")
    else:
        print(f"{a} is NOT a prime number.") """
        
