#1.Create a dictionary to store the names of 5 students as keys and their marks as values. Print all keys and values.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
for i,j in a.items():
    print(i,j) """
#2.Write a Python program to access the value of a specific key in a dictionary.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=input(f"enter the key:")
for i,j in a.items():
    if b in i:
        print(i,j) """
#33.How do you add a new key-value pair to a dictionary? Give an example.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
a["sree"]=90
a["kar"]=89
print(a) """
#4.Write a program to remove a key from a dictionary using pop().
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
a.pop("lime")
print(a["santhosh"]) """
#5.Explain the difference between dict.get() and direct key access dict[key].
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
print(a.get("santhosh","#n/a"))
#get doest not return error """
#6.Write a program to check if a given key exists in a dictionary.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=input(f"enter key:")
if b in a.keys():
    print(f"given key available in dict")
else:
    print(f"given key not available in dict") """
#6A.Write a program to check if a given value exists in a dictionary.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=int(input(f"enter value:"))
if b in a.values():
    print(f"given key available in dict")
else:
    print(f"given key not available in dict") """
#7.Create a dictionary and print only the keys using a loop.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
for i,j in a.items():
    print(i) """
#8.Write a program to count the frequency of each character in a string using a dictionary.
""" a=input(f"enter the string:")
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for v,w in b.items():
    print(f"{v}:{w}") """
#9.Merge two dictionaries into one in Python.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b={"srens":45}
a.update(b)
print(a) """
#10.Write a program to find the maximum and minimum values in a dictionary.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=0
for i in a.values():
    if i>b:
        b=i
for v,w in a.items():
    if w==b:
        print (v,w)
min_val = 0
for j in a.values():
    if j<min_val:
        min_val=j
for v,w in a.items():
    if w==min_val:
        print (v,w) """
#11.Convert two lists into a dictionary (list of keys and list of values).
""" a=["santhosh","prabhaat","karthik"]
b=[98,89,76]
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
print(c) """
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=list(a.items())
print(b) """
#12.Write a program to sort a dictionary by its values in ascending order.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=[]
for i in a.values():
    b.append(i)
    b.sort()
u={}
for j in b:
    for v,w in a.items():
        if w==j:
            u[v]=w
print(u) """
#13.How can you remove all elements from a dictionary? Demonstrate with code.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
a.clear()
print(a) """
#14.Write a program to update the value of an existing key in a dictionary.
""" a={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
a["santhosh"]=67
print(a) """
#15.Write a dictionary comprehension to create a dictionary of squares for numbers 1 to 10.
""" a={}
for i in range(1,10):
    a[i]=i*i
print(a) """
#16.Create a nested dictionary to store student details like name, age, and marks. Access specific values.

""" students={
    "name":"santhosh",
    "Age":36,
    "Dept":"data",
    "Teacher":["prabhaat","santhosh","shanthi"],
    "Subject":{
        "Maths":"prabhaat",
        "English":"santhosh",
    }}
students["Subject"]["maths"]="ramya"
print(students) """
#17.Write a program to invert a dictionary (swap keys and values).
""" students={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b={}
for i,j in students.items():
    b[j]=i
print(b) """
#18.Write a program that takes a list of dictionaries (each representing a student with name & marks) and finds the student with the highest marks.
""" students={"santhosh":34,
   "prabhaat":67,
   "sreekutty":90,
   "lime":43,
   "shankar":13}
b=0
for i in students.values():
    if i>b:
        b=i
for v,w in students.items():
    if w==b:
        print(f"{v}:{w}") """
#20.Write a program to group words by their length using a dictionary. Example: ["cat","dog","lion","tiger"] → {3:["cat","dog"], 4:["lion"], 5:["tiger"]}.
""" b=["cat","dog","lion","tiger"]
c={}
for i in b:
    v=len(i)
    if v not in c:
        c[v]=[]
    c[v].append(i)
print(c)
 """
""" b=["cat","dog","lion","tiger","santhoshsh"]
a={}
for i in b:
    c=len(i)
    if c not in a:
        a[c]=[]
    a[c].append(i)
print(a) """





    

