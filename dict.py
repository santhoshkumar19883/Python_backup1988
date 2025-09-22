""" students={
    "name":"santhosh",
    "Age":36,
    "Dept":"data",
    "Teacher":["prabhaat","santhosh","shanthi"],
    "Subject":{
        "Maths":"prabhaat",
        "English":"santhosh",
    }
} """

""" students['Subject']['Physics']='shanthi'
x=students.keys()
print(students) """
#values
""" x=students.values()
print(x)
 """
""" for x in students.keys():
    if x == "Subject":
        print(students[x]) """

#Create a dictionary to store the names of 5 students as keys and their
#marks as values. Print all keys and values.
""" def students_name():
    students = {
        "Santhosh": 85,
        "Prabhat": 90,
        "Karthik": 78,
        "Lakshmi": 92,
        "Anitha": 88
        }
    print("Student Names (Keys):")
    for name in students.keys():
            print(name)
def students_marks():
    students = {
        "Santhosh": 85,
        "Prabhat": 90,
        "Karthik": 78,
        "Lakshmi": 92,
        "Anitha": 88
        }
    print(f"students marks:")
    for marks in students.values():
        print(marks)
print(students_name())
print(students_marks()) """

#1.Create a dictionary to store the names of 5 students as keys and their marks as values. Print all keys and values.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,
   "priya":88,
   "ramya":82}
print(a) """
#2.Write a Python program to access the value of a specific key in a dictionary.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,
   "priya":88,
   "ramya":82}
b=input(f"enter the name:")
if b in a:
    print(f"name of {b}, and the marks{a[b]}")
else:
    print(f"no name deducted") """
#Write a Python program to access the value of a specific key in a dictionary.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
a["shan"]=90
print(a) """
#Write a program to remove a key from a dictionary using pop().

""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
a.pop("santhosh")
print(a) """
#Explain the difference between dict.get() and direct key access dict[key].
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
print(a.get("santhosh")) """
#Write a program to check if a given key exists in a dictionary.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,
   "priya":88,
   "ramya":82}
b=input(f"enter the name:")
if b in a:
    print(f"given name exist")
else:
    print(f"given name not exist") """
#Create a dictionary and print only the keys using a loop.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,
   "priya":88,
   "ramya":82}
for i in a.keys():
    print(i) """
#Write a program to count the frequency of each character in a string using a dictionary.
""" a=input('enter string')
b={}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i]=1
print(b) """
#Merge two dictionaries into one in Python.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
b={"priya":88,
   "ramya":82}
a.update(b)
print(a) """
#10.Write a program to find the maximum and minimum values in a dictionary.

""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
b=0
for i, j in a.items():
    if j>b:
       b=j
       d=i
print({d:b})
c=list(a.values())[0]
for i, j in a.items():
    if j<c:
        c=j
        e=i
print({e:c}) """
""" keys = ["santhosh", "prabhaat", "shankar"]
values = [98, 76, 87] """

# Convert to dictionary
""" a = {}
for i in range(len(keys)):
    a[keys[i]] = values[i]

print(a)
 """

#13.How can you remove all elements from a dictionary? Demonstrate with code.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
a.clear()
print(a) """
#14.Write a program to update the value of an existing key in a dictionary.
""" a={"santhosh":98,
   "prabhaat":76,
   "shankar":87,}
a["santhosh"]=88
print(a) """
#15.Write a dictionary comprehension to create a dictionary of squares for numbers 1 to 10.
""" b={}
for i in range(1,11):
    b[i]=i*2
print(b)    """
#20.Write a program to group words by their length using a dictionary. Example: ["cat","dog","lion","tiger"] → {3:["cat","dog"], 4:["lion"], 5:["tiger"]}.
a=["cat","dog","lion","tiger","rat"]
b={}
for i in a:
    b[i]=len(i)
print(b)
c={}
for j,v in b.items():
    if v not in c:
        c[v]=[]
    c[v].append(j)
print(c)
    
