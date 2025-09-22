#1. Given the list nums = [10, 20, 30, 40, 50], write a slice to get the first three elements.
""" nums = [10, 20, 30, 40, 50]
print(nums[0:3]) """
#2. From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.
""" nums = [1, 2, 3, 4, 5]
print(nums[1:]) """
#3. Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue'].
""" colors = ['red', 'green', 'blue', 'yellow']
print(colors[1:3]) """
#4. From fruits = ['apple', 'banana', 'cherry', 'mango'], use slicing to get ['banana', 'cherry', 'mango'].
""" fruits = ['apple', 'banana', 'cherry', 'mango']
print(fruits[1:]) """
#5. Given nums = [5, 10, 15, 20, 25, 30], slice to get the last two elements only.
""" nums = [5, 10, 15, 20, 25, 30]
print(nums[-1:-3:-1]) """
#6. Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to get every second element.
""" nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[0::2]) """
#7. From the list letters = ['a', 'b', 'c', 'd', 'e', 'f'], get the elements from index 2 to the end.
""" letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[1:]) """
#8. Given nums = [10, 20, 30, 40, 50, 60, 70], use slicing to reverse the list.
""" nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[-1::-1]) """
#9. From data = [1, 3, 5, 7, 9, 11, 13], slice the list to get elements starting from index 1 up to index 5
#with a step of 2.
""" data = [1, 3, 5, 7, 9, 11, 13]
print(data[0:5:2]) """
#12. From nums = [1, 2, 3, 4, 5], slice the list to get [4, 3, 2] using a negative step value.
""" nums = [1, 2, 3, 4, 5]
print(nums[-2:0:-1]) """
#13. Given nested = [[1, 2], [3, 4], [5, 6]], slice to get the first two sublists.
""" nested = [[1, 2], [3, 4], [5, 6]]
print(nested[:2]) """
#14. From nums = list(range(1, 21)), use slicing to get the last 5 elements in reverse order.
""" x=list(range(1,21))
print(x[-1:-6:-1]) """

#Append

#Create a list of fruits: ["apple", "banana"]. Append "mango" to the list and print the final list.

""" fruit=["apple", "banana"]
fruit.append("mango")
print(fruit) """
#Ask the user to enter 3 favorite colors one by one. Append each to a list and display the list.
""" b=[]
for i in range(3):
    c=input(f"input item:{i+1}")
    b.append(c)
print(b) """
#Create an empty list. Append the square of numbers from 1 to 5 into it using a loop. Print the list.
""" 
 """
#4. Append Numbers Based on Condition
#From the range 1 to 20, append only numbers divisible by 3 into a list. Print the final list.
""" b=[]
for i in range(1,21):
    if i%3==0:
        b.append(i)
print(b) """

""" list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
print(list1) """
#6. Append Dictionaries to a List
#Write a program that takes 2 user inputs: name and age. Append them as a dictionary to a list. Repeat for 3
#users.
""" a=[]
for i in range(3):
    name=(input(f"enter name:{i+1}"))
    age=(int(input(f"enter age:{i+1}")))
    b=(f"name:{name},age:{age}")
    a.append(b)
print(a) """
#10. Append and Sort
#Take 5 numbers as input from the user, append them to a list. Sort the list and print it.
""" a=[]
for i in range(3):
    b=int(input(f"enter number:{i+1}"))
    a.append(b)
a.sort(reverse=True)
print(a) """
#9. Using Append with Condition from List
#Given: scores = [45, 67, 23, 90, 88]. Append only scores > 50 to a new list called passed.
""" scores = [45, 67, 23, 90, 88]
passed=[]
for i in scores:
    if i>50:
        passed.append(i)
print(passed)
 """
#2. Write a Python program to remove the number 3 from this list: numbers = [1, 2,
#3, 4, 5]
""" numbers = [1, 2,3, 4, 5]
del numbers[2]
print(numbers) """
#6. How would you remove all occurrences of the value 5 from the list: nums = [5, 1,
#2, 5, 3, 5, 4]?
""" nums = [5, 1,2, 5, 3, 5, 4]
nums.clear()
print(nums)
 """
""" fruits = ['banana','orange', 'apple', 'mango']
for i in fruits:
    if i=='apple':
        fruits.remove(i)
print(fruits) """
#12. Given a list of dictionaries, remove all dictionaries where 'status' is 'inactive'.
a={"name":"santhosh",
   "status":"inactive",
   "name":"prabhat",
   "status":"active"}
""" c=list(a)
b=[]
for i in c:
    if i["status"]!="inactive":
        b.append(i)
print(b)
 """

#1. Write a program to check if a number is positive or negative.
""" a=int(input())
if a>0:
    print(f"{a} is positive")
else:
    print(f"{a} is nagative") """
#2. Write a Python program to check whether a number is even or odd using if-else.
""" a=int(input())
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd") """
#3. Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and
#60, and 'Senior' if 60 or above.
""" a=int(input(f"enter age:"))
if a<18:
    print(f"you are minor")
elif a>18 and a<60:
    print(f"you are adult")
else:
    print(f"you are a senior") """
#5. Write a Python program to check if a number is divisible by 3 and 5 both.
""" a=int(input("enter the number:"))
if a%3==0 and a%5==0:
    print("given number is divisible by both 3 and 5")
else:
    print("given number is not divisible by both 3 and 5") """
#7. Write a program that takes input for two numbers and prints which one is greater or if they are
#equal.
""" a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater") """
#8. Write a program that checks whether a year is a leap year or not.
""" a=int(input("enter year:"))
if a%4==0:
    print(f"{a} is leap year")
else:
    print(f"a is not a leap year") """
#9. Write a Python program that simulates a simple login system with a stored username and
#password. Use if-else to check credentials.
""" username="santhosh"
pasword="31121988"
a=input(f"enter user name:")
b=input(f"enter password:")
if a==username and b==pasword:
    print(f"you are authorised person")
else:
    print(f"you are not authorised person") """