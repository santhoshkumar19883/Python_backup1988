""" x=input(f"enter names:")
y=list(x)
for i in y:
    print(i) """
""" x=(1,2,3,4,5)
y=list(x)
y[1]=6
z=tuple(y)
print(z) """
#convert tuple to list and editing names
""" a=[]
for i in range(6):
    b=input(f"enter name :{i+1}")
    a.append(b) """
""" a[2]="santhosh"
d=tuple(a)
print(d) """
""" z=int(input(f"enter number:"))
a[z]=input(f"name change:")
d=tuple(a)
e=list(d)
d.remove[4]
print(e)    """
#Tuple slicing – Given nums = (10, 20, 30, 40, 50, 60), print only the middle 4 elements.
"""nums = (10, 20, 30, 40, 50, 60)
a=len(nums)//2 - 2
b=len(nums)//2 + 2
print(nums[a:b])"""
nums = (10,10, 20, 30, 40, 50, 60, 40)
b=list(nums)
""" b=list(nums) """
""" for i in b: """
""" c=int(input(f"number to remove:"))
b.remove(c)
print(b) """
""" for i in b:
    if i==i+1:
        b.remove(i) """
""" c=[]
for i in b:
    if i not in c:
        c.append(i) """
""" print(nums) """
c=int(input(f"enter number to remove:"))
while c in b:
    b.remove(c)
print(b)




