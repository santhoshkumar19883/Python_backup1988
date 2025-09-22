""" thislist = ["apple", "banana", "cherry", 23, "cherry"]
for i in thislist:
    print(i) """
""" thislist[2]="santhosh"
print(len(thislist))
print(type(thislist)) """
a=["santhosh","sa","prabhat"]
b=["sreenika","ramya"]
print(a+b)
""" for i in range(10,0,-1):
    print(i)
 """
#Given the list nums = [10, 20, 30, 40, 50], write a slice to get the first three elements.
""" a=[10, 20, 30, 40, 50]
print(a[0:3]) """
""" a=[10, 20, 30, 40, 50]
b=0
for i in range (len(a)):
     b=b+a[i]

     
print(b)
    """
""" a=["santhosh","prabhaat","ramya","sreekutty"]
for i in range(len(a)):
    print(a[i]) """
#From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.
""" nums = [1, 2, 3, 4, 5]
print(nums[1:])
for y in nums:
    if y==2:
        pass
    else:
        print(y) """
#returning with out sunday
""" days=["mon","tue","wed","Thurs","friday","saturday","sunday"]
for x in range(len(days)):
    if x==6:
        pass
    else:
        print(days[x]) """
#Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue'].
""" color=['red', 'green', 'blue', 'yellow']
for i in enumerate(color):
    print(i, color) """
""" print(color[1:3]) """
""" nums = [5, 10, 15, 20, 25, 30]
print(nums[4:]) """
#Append a String
#Create a list of fruits: ["apple", "banana"]. Append "mango" to the list and print the final list.
""" fruits=["apple","banana"]
fruits.append("mango")
for i in fruits:
    print(i) """
#2. Append User Input
#Ask the user to enter 3 favorite colors one by one. Append each to a list and display the list.
""" a=[]
for i in range(3):
    b=input(f"enter name{i+1}")
    i=a.append(b)
print(a) """
#3. Append in a Loop
#Create an empty list. Append the square of numbers from 1 to 5 into it using a loop. Print the list.
""" a=[]
for i in range(1,6):
    a.append(i**2)
print(a) """
#4. Append Numbers Based on Condition
#From the range 1 to 20, append only numbers divisible by 3 into a list. Print the final list.
""" a=[]
for i in range(1,21):
    if i%3==0:
        a.append(i)
print(a) """
#list1 = [1, 2]
#list2 = [3, 4]
#Use append() to add list2 to list1. Print list1. What will be the length of list1?
""" list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
print(list1)
print(len(list1)) """
#7. Append to Nested List
#Create a list: students = [["Alice", 85], ["Bob", 90]]. Append a new student ["Charlie", 88] using append().
""" student=[["Alice", 85], ["Bob", 90]]
student.append(["Charlie", 88])
print(student) """
#Given: scores = [45, 67, 23, 90, 88]. Append only scores > 50 to a new list called passed.
""" scores = [45, 67, 23, 90, 88]
b=[]
for i in scores:
    if i>50:
        b.append(i)
print(b) """
#Use nested loops to create a 3x3 matrix:
#a=[[0, 1, 2], [0, 1, 2], [0, 1, 2]]

""" c=[]
for i in range(3):
    b=[]
    for x in range(3):
        value=int(input("Enter value:"))
        b.append(value)
    c.append(b)

print(c)"""
""" c=[]
for i in range(3):
    b=[]
    for y in range(3):
        num=int(input("number:"))
        b.append(num)
    c.append(b)
print(c) """
#use for loop to get a result with single list of this nested list a= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
""" a= [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
b=[]
for i in a:
    for y in i:
        b.append(y)
print(b) """

""" country=[]
for i in range(10):
    name=input(f"enter country name:{i+1}")
    country.append(name)
    d=tuple(country)
print(d) """
a=set()
for i in range(5):
    b=int(input(f"input is: {i+1}"))
    a.add(b)
    c=list(a)
print(c)



