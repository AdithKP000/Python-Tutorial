"""3.	Write data to an excel file."""
import pandas as pd

entries = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
names = ['A', 'B', 'C']

df = pd.DataFrame(entries, index=names, columns=[f'Col{i+1}' for i in range(len(entries[0]))])
df.to_excel("output.xlsx", index=True)

print("Data written to output.xlsx")