""" def my_function(a, b):
  print(a + " " + b)

my_function("santhosh", "rajan")  """
""" def my_function(*a):
    print(f"my favourite subject:{a[2]}")
my_function("tamil","english","maths") """
""" def my_function(a,b,c):
    print(f"my youngest child is :"+ a)
my_function(b="santhosh",c="shankar",a="prabhaat") """
""" def my_function(**a):
    print(f"my last name is "+a["c"])
my_function("fad","fdfa","fdaf","dfae","fdafar",c="rajan") """
""" def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))  """
""" def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
my_function(5,6,c=9,d=9)
 """
""" def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(10))  # 120 """
#1.Write a function that takes a name as input and prints "Hello, <name>!".

""" def My_function(name):
    print(f"hello:{name}")
My_function("santhosh")
 """
#2.Write a function that takes two numbers and returns their product.
""" def product():
    a=int(input())
    b=int(input())
    print(a*b)
product() """
#3.Write a function that checks if a number is even or odd.
""" def odd_even():
    a=int(input(f"enter the number:"))
    if a%2==0:
        print(f"given number is even:")
    else:
        print(f"given number is odd")
odd_even() """
#4.Write a function that takes a list of numbers and returns the maximum number.
""" def max():
    c=[]
    b=0
    for i in range(5):
        a=int(input(f"enter numbers:{i}"))
        c.append(a)
        if a>b:
            b=a
    print(c)
    print(b)
max() """
#5.Write a function that counts the vowels in a given string.
""" def vowel():
    a=input(f"enter the string:")
    b=["a","e","i","o","u"]
    c=0
    for i in a:
        if i in b:
            c+=1
    print(c)
vowel()
 """
#7.Write a function that accepts any number of numbers (*args) and returns their average.
""" def average():
    c=0
    for i in range(5):
        a=int(input(f"enter numbers:"))
        c+=a
        d=c/5
    print(d)
average() """
#8.Write a function that accepts a dictionary of student names and marks, and returns the name of the student with the highest marks.
""" def Highmark():
    c={}
    for i in range(5):
        a=input(f"enter student names:")
        b=int(input(f"enter marks:"))
        c[a]=b
    d=0
    for j in c.values():
        if j>d:
            d=j
    for v,w in c.items():
     if w==d:
          print(f"{v}:{w}")
Highmark()
 """
#9.Write a function that takes a sentence and returns a dictionary with the word count of each word.
""" def word():
    a=input(f"enter the name:")
    c={}
    for i in a:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    print(c)
word()
 """
#10.Write a function that takes two lists and returns their intersection (common elements).
""" def intersection():
    a=input(f"enter the first list by space:")
    b=input(f"enter the first list by space:")
    c=[]
    for i in a:
        if i in b and i not in c:
            c.append(i)
    print(c)
intersection() """
#11.Write a function that returns another function which multiplies numbers by a given factor (closure).
def mul(factor):
    def Mul_by(n):
        return n*factor
    Mul_by(3)
mul(5)

