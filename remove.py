#2. Write a Python program to remove the number 3 from this list: numbers = [1, 2,
#3, 4, 5]
""" numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers) """
#What error is raised if you try to remove an element that doesn’t exist in the list
#using remove()?
#ValueError: list.remove(x): x not in list
#4. What is the difference between remove() and pop() in Python lists?
#pop() remove value from the elements order remove() remove the exact value from list
#5. Write a Python program to remove the first occurrence of a given element from a
#list.
""" numbers = [1, 2, 3, 4, 5]
numbers.pop(0)
print(numbers) """
#6. How would you remove all occurrences of the value 5 from the list: nums = [5, 1,
#2, 5, 3, 5, 4]?
""" numbers = [5, 1, 2, 5, 3, 5, 4]
while 5 in numbers:
    numbers.remove(5)
print(numbers) """
#7. Given a list of strings, remove the string 'apple' only if it exists. fruits = ['banana',
#'orange', 'apple', 'mango']
""" fruits = ['banana','orange', 'apple', 'mango']
fruits.remove('apple')
print(fruits) """
#8. What will be the output of the following code? Explain your answer: a = [1, 2, 3]
#a.remove(4)
""" a = [1, 2, 3]
a.remove(4)
print(a) """
#ValueError: list.remove(x): x not in list
#13. Write a program to remove all negative numbers from a list using a loop and
#remove().
""" a = [1, 2, 3,-1,4,-2,-5,-6]
for i in a[0:]:
    if i<0:
        a.remove(i)
print(i) """
""" b=[]
for i in range(len(a)):
    
    if a[i]>0:
        b.append(a[i])
print(b) """
#14. Explain why modifying a list with remove() while iterating over it may produce
#unexpected results. Provide an example.
a = [1, 2,2, 3,-1,4,-2,-5,-6]
b=[3]
for i in a[0:]:
    if b == i:
        b.append(i)
print(b)

