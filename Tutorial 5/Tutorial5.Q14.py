
""" 14. Write Python program to write the data given below to a CSV file
 Reg_no Name Sub_Mark1 Sub_Mark2 Sub_Mark3
 10001 Jack 76 88 76
 10002 John 77 84 79
 10003 Alex 74 79 81"""

import pandas as pd

data = [
    [10001, 'Jack', 76, 88, 76],
    [10002, 'John', 77, 84, 79],
    [10003, 'Alex', 74, 79, 81]
]

columns = ['Reg_no', 'Name', 'Sub_Mark1', 'Sub_Mark2', 'Sub_Mark3']

df = pd.DataFrame(data, columns=columns)

df.to_csv('students.csv', index=False)

print("CSV file 'students.csv' has been created successfully.")
