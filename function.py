""" def nameorder(fname,lname):
    print(fname+","+lname)
nameorder("santhosh","Rajan") """
""" def sum(a,b):
    return a*b
print(sum(5,6)) """
""" a=int(input())
b=int(input())
def sum(a,b):
    return a+b
print(sum(a,b)) """
""" p=int(input())
r=float(input())
t=float(input())
def pnr(p,r,t):
    return (p*r*t)/100
print(pnr(p,r,t)) """
""" for i in range(5):
    a=int(input(f"enter marks{i}"))
    b=b+a
    c=b/5
print(c) """
""" # creating average of 5 inputs marks
def avg():
    b=[]
    for i in range(5):
        a=int(input(f"enter marks{i+1}"))
        b.append(a)
        c=0
        for i in b:
            c=c+i
            d=c/5
    print(d)""" 
"""     print(b)
avg() """

""" def avg(a):
    for i in a:
        i=i+1
        b=i/5
        return b
print(avg(a))  """

""" def nameorder(fname,lname):
    print(fname+","+lname)
nameorder("5","6") """

""" def my_function(kids):
    print("The youngest child is " + kids[3])
my_function(["santhosh","prabhaat","priya","sankar","senthisl"]) """
""" def my_func(salary):
    a=0
    for i in salary:
        i=i+1
        a=i
    print(a)
my_func([14000,15000,16000,17000,18000]) """

#1.Write a function that takes a name as input and prints "Hello, <name>!".
""" def name():
    a=input()
    print(f"Hello,<{a}>!")
name() """
#2.Write a function that takes two numbers and returns their product.
""" def product():
    a=int(input(f"enter first number:"))
    b=int(input(f"enter second number:"))
    print(f"answer is :{a*b}")
product() """
#3.Write a function that checks if a number is even or odd.
""" def evenorodd():
    a=int(input(f"enter the number to check:"))
    if a%2==0:
        print(f"{a} is even number")
    else:
        print(f"{a} is odd number")
evenorodd() """
#4.Write a function that takes a list of numbers and returns the maximum number.
""" def maxnumber():
    a = []  
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        a.append(num)
        t=a[0]
    for i in a:
        if i > t:
            t=i
    print(t)
maxnumber() """

#5.Write a function that counts the vowels in a given string.
""" def vowels():
    a=input(f"enter string:")
    b=['a','e','i','o','u']
    count=0
    for i in a:
        if i in b:
            count=count+1
    print(count)
vowels()
 """
""" def sum():
    a=0
    for i in range(5):
        b=int(input(f"enter Chicks Placed:{i}"))
        a=b+a
    print(a)
    d=0
    for j in range(5):
        c=int(input(f"enter Mean Age:{i}"))
        d=c+a
    print(d)
sum() """
#8.Write a function that accepts a dictionary of student names and marks, and returns the name of the student with the highest marks.
""" def high_marks():
    c={}
    for i in range(5):
        a=input(f"enter name:{i}")
        b=int(input(f"enter marks:"))
        c[a]=b
    print(c)
    x=0
    for j in c.values():
        if j>x:
            x=j
    for key,value in c.items():
        if value==x:
            print(f"{key}:{value}")
high_marks() """
#1.Write a function that takes a name as input and prints "Hello, <name>!".
""" def Hello(name):
    print(f"Hello,{name}")
Hello("santhosh") """
#Write a function that takes two numbers and returns their product.
""" def product():
    a=int(input())
    b=int(input())
    c=a*b
    print(c)
product()   """
#3.Write a function that checks if a number is even or odd.
""" def even():
    a=float(input())
    if a%2==0:
        print(f"given {a} is even")
    else:
        print(f"given {a} is add")
even() """
#4.Write a function that takes a list of numbers and returns the maximum number.
def maxnumber():
    a = []  
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        a.append(num)
        t=a[0]
    for i in a:
        if i > t:
            t=i
    print(t)
maxnumber()

