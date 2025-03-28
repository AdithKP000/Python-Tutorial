"""13. Consider a CSV file ‘employee.csv’ with the following
columns(name, gender, start_date ,salary, team)
Write commands to do the following using panda library.
1. print first 7 records from employees file
2. print all employee names in alphabetical order
3. find the name of the employee with highest salary
4. list the names of male employees
5. Display to which all teams employees belong"""

import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def process_employee_data(file):
    df = load_data(file)
    print("First 7 records:")
    print(df.head(7))
    print("\nEmployees in alphabetical order:")
    print(df.sort_values('name')['name'])
    print("\nEmployee with highest salary:")
    print(df.loc[df['salary'].idxmax(), 'name'])
    print("\nMale employees:")
    print(df[df['gender'] == 'Male']['name'])
    print("\nTeams employees belong to:")
    print(df['team'].unique())

employee_file = "employee.csv"
process_employee_data(employee_file)
