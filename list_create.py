a=["santhosh","prabhat","sree",[23, 45, 'çoimbatore',['gandhipuram','sulur','sai baba'], 76],"ream","sakthi"]
a.append([23,45,'çoimbatore',76])
""" print(a) """

print(a[3][3][1])
""" b=a[3]
for i in b:
    print(i) """
# append student names
""" student=[]
for i in range(5):
    a=input(f"enter studnet{i+1}:")
    student.append(a)

print(student) """
#total for input marks
""" Marks=[]
total=0
for i in range(5):
    a=int(input(f"enter marks{i+1}:"))
    Marks.append(a)
    total=total+a
print(total) """
""" Marks=[]
for i in range(5):
    Marks.append()
print(Marks) """
""" a=["santhosh","prab","sree"]
b=["23","45","67"]
for i in a:
    for x in b:
        print(i,x) """
""" a=["sakthi","easwar","priya"]
b=[45,56,78]
for x in a:
    for y in b:
        print(x,y) """
#Given the list nums = [10, 20, 30, 40, 50], write a slice to get the first three elements.
""" a=[10, 20, 30, 40, 50]
b=0
for i in a[0:3]:
    print(i) """
    
#From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.
""" num=[1, 2, 3, 4, 5]
for i in num[1:]:
    print(i) """
#Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue'].
""" color=['red', 'green', 'blue', 'yellow']
for i in color[1:3]:
    print(i) """
#From fruits = ['apple', 'banana', 'cherry', 'mango'], use slicing to get ['banana', 'cherry', 'mango'].
""" fruits=['apple', 'banana', 'cherry', 'mango']
for i in fruits[1:]:
    print(i) """
#Given nums = [5, 10, 15, 20, 25, 30], slice to get the last two elements only.
""" num=[5, 10, 15, 20, 25, 30]
for i in num[-2:]:
    print(i) """
#Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to get every second element.
""" num=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num[1::2]:
    print(i) """
#From the list letters = ['a', 'b', 'c', 'd', 'e', 'f'], get the elements from index 2 to the end.
""" letter=['a', 'b', 'c', 'd', 'e', 'f']
for i in letter[1:]:
    print(i) """
#Given nums = [10, 20, 30, 40, 50, 60, 70], use slicing to reverse the list.
""" num=[10, 20, 30, 40, 50, 60, 70]
for i in num[-1::-1]:
    print(i) """
#From data = [1, 3, 5, 7, 9, 11, 13], slice the list to get elements starting from index 1 up to index 5
#with a step of 2
""" data=[1, 3, 5, 7, 9, 11, 13]
for i in data[1:5:2]:
    print(i) """
#Given nums = [100, 200, 300, 400, 500, 600], use slicing to get [200, 300, 400] without
#specifying the start index explicitly.
""" nums = [100, 200, 300, 400, 500, 600]
for i in nums[1:4]:
    print(i) """
#Given nums = [1, 2, 3, 4, 5], what will be the output of nums[10:]? Explain why.
""" a=[1, 2, 3, 4, 5]
print(a[10:]) """
#output only [] because only 5 items in the list. how it is start 10
#From nums = [1, 2, 3, 4, 5], slice the list to get [4, 3, 2] using a negative step value.
""" a=[1, 2, 3, 4, 5]
for i in a[-2:-5:-1]:
    print(i) """
#Given nested = [[1, 2], [3, 4], [5, 6]], slice to get the first two sublists.
""" num=[[1, 2], [3, 4], [5, 6]]
print(num[:2])
for i in num[:2]:
    print(i) """
#From nums = list(range(1, 21)), use slicing to get the last 5 elements in reverse order.

""" a=list(range(1,21))
for i in a[-1:-6:-1]:
    print(i) """
#Given nums = [10, 20, 30, 40, 50], what happens if you slice it as nums[-1:-4]? Explain and fix it
#to get [50, 40, 30].
""" a=[10, 20, 30, 40, 50]
for i in a[-1:-4:-1]:
    print(i) """