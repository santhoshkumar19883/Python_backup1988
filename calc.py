def calc():
    a=float(input(f"enter first number:"))
    b=float(input(f"enter second number:"))
    ope=input(f"enter operator:")
    if ope == "+":
        print(a+b)
    elif ope == "-":
        print(a-b)
    elif ope == "*":
        print(a*b)
    elif ope == "/":
        print(a/b)
    else:
        print("operator wrong")
calc()