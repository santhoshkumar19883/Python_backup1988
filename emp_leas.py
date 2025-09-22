import pandas as pd

df = pd.read_excel("employees.xlsx")

name_input = input("Enter Employee Name (min 3 letters): ").strip()

if len(name_input) < 3:
    print("Please enter at least 3 letters for searching.")
else:
    employees = df[df["Name"].str.contains(name_input, case=False, na=False)]

    if not employees.empty:
        print("\nMatching Employee(s):\n")
        print(employees.to_string(index=False))
    else:
        print("No employee found with that name!")