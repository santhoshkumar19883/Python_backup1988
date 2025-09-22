import pandas as pd

df = pd.read_excel("employees.xlsx")
emp_id = int(input("Enter Employee ID: "))

# Search for the employee
employee = df[df["EmpID"] == emp_id]

if not employee.empty:
    print("\nEmployee Details:\n")
    # Display all columns in table format
    print(employee.to_string(index=False))
else:
    print("Employee ID not found!")