""" a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater") """
m=int(input())
p=int(input())
t=int(input())
e=int(input())
c=int(input())
total=(m+p+t+e+c)/500*100
if total>75:
    print(f"{total: .2f} passed with distinc")
elif total<75 and total>60:
    print(f"{total: .2f} passed with first class")
elif total<60 and total>35:
    print(f"{total: .2f} just pass")
else:
    print(f"{total: .2f} fail")

""" a=int(input())
if(a%2==0):
    print(f"{a} is even")
else:
    print(f"{a} is odd number") """



""" a=int(input())
if(a<0):
    print(f"{a} is nagative")
else:
    print(f"{a} is positive") """
""" age=int(input())
if(age<18):
    print(f"{age} is minor")
elif(age>18) and age<60:
    print(f"{age} is a adult")
else:
    print(f"{age} is senior") """
""" a=int(input())
if(a>90) and (a<100):
    print(f"{a} A grade")
elif(a>80) and (a<89):
    print(f"{a} B Grade")
elif(a>70) and (a<79):
    print(f"{a} C Grade")
elif(a>60) and (a<69):
    print(f"{a} D Grade")
else:
   print(f"{a} fail")  """
""" a=int(input())
b=int(input())
if(a>b):
    print(f"{a} is greater than {b}")
elif(b>a):
    print(f"{b} is greater than {a}")
else:
    print(f"both are equal")
 """
""" year=int(input())
if(year%4==0):
    print(f"{year} is leap year")
else:
    print(f"{year} not leap year")
 """
""" a=float(input())
b=float(input())
ope=input("enter operator: ")
if ope=="+":
    print(f"answer is ,{a+b: .1f}")
elif ope=="-":
    print(f"answer is ,{a-b: .1f}")
elif ope=="*":
    print(f"answer is ,{a*b: .1f}")
elif ope=="/":
    print(f"answer is ,{a/b: .1f}")
else:
    print(f"wrong input operator") """
""" username="santhosh"
password="Sant12"
a=input(f"enter username:")
b=input(f"enter password:")
if(a==username) and (b==password):
    print(f"you are authenticated")
else:
    print(f"you are not authenticated{a} {b} wrong") """
""" a=int(input())
print(len[(int(a))) """
""" num = input("Enter a number: ")

remaining = num[:-1]

result = int(remaining) - 1

print(result) """
""" a="santhosh"
print(reversed(a)) """