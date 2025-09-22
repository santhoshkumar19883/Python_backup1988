#Print numbers from 0 to 9 using range.
""" for i in range(0,10):
    print(i) """
#Print even numbers from 2 to 10 using range.
""" for i in range(2,11,2):
    print(i) """
#Print all numbers from 5 to 15 using range.
""" for i in range(5,16):
    print(i) """
#Create a list from 0 to 5 using range and list() function.
""" a=[0,1,2,3,4,5]
for i in a:
    print(i) """
#What will range(5, 15, 2) produce? Write a program to print it
""" for i in range(5,12,2):
    print(i) """
#Use range to print numbers in reverse from 10 to 1.
""" for i in range(10,0,-1):
    print(i) """
#Print all multiples of 3 between 1 and 30 using range.
""" for i in range(3,31,3):
    print(i) """
#What is the output of list(range(10, 0, -2))? Explain.
""" for i in range(10,0,-2):
    print(i) """
#Use a for loop and range to calculate the sum of numbers from 1 to 100.
""" b=0
for i in range(1,101):
    b=b+(i*2)
print(b) """
#Check if a number exists in a given range or not (e.g., is 15 in range(10, 21)?).
a=int(input(f"enter number:"))
for i in range(1,100):
    if i==a:
        print("available")
        break
else:
    print("not available")
        
