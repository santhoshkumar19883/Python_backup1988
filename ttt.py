#Given the list nums = [10, 20, 30, 40, 50], write a slice to get the first three elements.
""" num=[10, 20, 30, 40, 50]
for i in num[0:3]:
    print(i) """
#From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.
""" num=[1,2,3,4,5]
for i in num[1:]:
    print(i) """
#Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue']. 
""" list=['red','green','blue','yellow']
for i in list[1:3]:
    print(i) """
#Given nums = [5, 10, 15, 20, 25, 30], slice to get the last two elements only.
""" list=[5,10,15,20,25,30]
for i in list[-2:]:
    print(i) """
#Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to get every second element.
""" list=[0,1,2,3,4,5,6,7,8,9]
for i in list[0:10:2]:
    print(i)` """

#12. From nums = [1, 2, 3, 4, 5], slice the list to get [4, 3, 2] using a negative step value.`n
""" list=[1,2,3,4,5]
for i in list[-2:-5:-1]:
    print(i) """

#1. Write a program to check if a number is positive or negative.
""" a=int(input())
if a>=0:
    print("a is possitive")
else:
    print("a is nagative") """
#Write a Python program to check whether a number is even or odd using if-else.
""" 
 """


#Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and
#60, and 'Senior' if 60 or above
n=int(input())
if n<18:
    print(f"{n} is a minor")
elif n>18 and n<60:
    print(f"{n} is a adult")
else:
    print(f"{n} is a senior")
    