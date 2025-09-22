import pandas as pd
df = pd.read_excel("employees.xlsx")
emp_id = int(input("Enter Employee ID: "))

# Search for the employee
employee = df[df["EmpID"] == emp_id]

if not employee.empty:
    emp = employee.iloc[0]  # Get the first row (since EmpID is unique)
    print("\nEmployee Details:")
    print(f"EmpID     : {emp['EmpID']}")
    print(f"Name      : {emp['Name']}")
    print(f"Gender: {emp['Gender']}")
    print(f"Department: {emp['Department']}")
    print(f"Business Title: {emp['Business Title']}")
    print(f"ADDRESS: {emp['ADDRESS']}")
    print(f"WorkdayID: {emp['Workday ID']}")
    print(f"PL Balance: {emp['PL']}")
    print(f"SL Balance: {emp['SL']}")
    print(f"CL Balance: {emp['CL']}")
    print(f"RH Balance: {emp['RH']}")
else:

    print("Employee ID not found!")