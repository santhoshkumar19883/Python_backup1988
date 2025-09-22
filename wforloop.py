#1. Print numbers 1 to 10 in list using a for loop.
""" for i in range(1,11):
    print(i) """
#2. Print even numbers from 1 to 20 using a for loop.
""" for i in range(0,21,2):
    print(i) """
#3. Find the sum of numbers from 1 to 100 using a for loop.
""" a=0
for i in range(1,101):
    a=i+a
print(a) """
#4. Print the multiplication table of 5 using a for loop.
""" a=0
for i in range(1,11):
    a=i*5
    print(f"{i}--{a}") """
#5. Print each character of a string using a for loop.
""" a=input()
for i in a:
    print(i) """
#6. Reverse a string using a for loop.
""" a=input()
for i in a[::-1]:
    print(i)
 """
#7. Count the number of vowels in a string using a for loop.
""" a=input()
b=['a','e','i','o','u']
c=0
for i in a:
    if i in b:
        c=c+1
print(c)
 """
#8. Find the largest number in a list using a for loop.
""" b=0
for i in range(10):
    a=int(input(f"enter numbers:{i+1}"))
    if a>b:
        b=a
print(b) """
#9. Print all elements of a 2D list using nested for loops.
""" a=[1,2,4,5,6]
b=[6,8,9,10]
for x in a:
    for y in b:
        print(x,y) """
#12. Remove duplicates from a list using a for loop (without using set).
""" b=[]
for i in range(1,11):
    a=int(input(f"enter numbers:{i}"))
    if a not in b:
        b.append(a)
print(b) """
#14. Flatten a nested list (one level) using a for loop.
a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)    
flattened = []

for sublist in c:        # take each list inside
    for item in sublist:      # take each element from that list
        flattened.append(item)

print(flattened)