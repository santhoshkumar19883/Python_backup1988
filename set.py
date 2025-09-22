#1. How do you create an empty set in Python? Why is {} not used for this purpose?
""" a={}
print(a) """
#2. Write a Python program to create a set with elements 1, 2, 3, 4, 5.
""" a={1, 2, 3, 4, 5}
print(a) """
#3. How can you check if a specific element exists in a set?
""" a={1, 2, 3, 4, 5}
print(2 in a) """
#5. Write a program to iterate through all elements of a set using a for loop.
a={1, 2, 3, 4, 5}
""" a={1, 2, 3, 4, 5}
for i in a:
    print(i) """
#6. Create a set containing the numbers 10, 20, 30, then add the number 40 to it.
""" a={10,20,30}
a.add(40)
print(a) """
#7. How do you add multiple elements {50, 60, 70} to an existing set?
""" a={50,60,70}
b={80,90,100}
a.update(b)
print(a) """
#9. Write a program to remove an element 30 from a set using remove(). What happens if
#the element is not found?
""" a={10,20,40}
a.remove(40)
print(a) """
#Keyerror

#10. Write a program to remove an element 30 from a set using discard(). What happens if
#the element is not found?
""" a={10,20,40}
a.discard(30)
print(a) """
#11. How do you remove and return a random element from a set? Write an example.
""" a={10,20,40}
a.pop()
print(a) """
#12. Write a program to clear all elements from a set without deleting the set itself.

""" a={10,20,40}
a.clear()
print(a) """
#13. How do you find the union of two sets {1, 2, 3} and {3, 4, 5}?
""" a={1, 2, 3}
b={3, 4, 5}
c=a.union(b)
print(c) """
#14. How do you find the intersection of two sets {1, 2, 3} and {2, 3, 4}?
""" a={1, 2, 3}
b={3, 4, 5}
c=a.intersection(b)
print(c) """
#15. Write a program to get elements present in set A but not in set B (Difference).
""" a={1, 2, 3}
b={3, 4, 5}
c=a-b
print(c) """
#16. Write a program to get elements that are in either set A or set B but not in both
#(Symmetric Difference).
""" a={1, 2, 3}
b={3, 4, 5}
print(a^b) """
#17. How do you check if one set is a subset of another? Give an example.
a={1, 2, 3}
b={3, 4, 5}
print(a.issubset(b))

