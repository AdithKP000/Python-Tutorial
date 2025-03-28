"""2.	Create a dataframe from a list of data and set the index."""

import pandas as pd

def generate_df(entries, labels):
    try:
        return pd.DataFrame(entries, index=labels, columns=[f'C{i+1}' for i in range(len(entries[0]))])
    except Exception as err:
        return str(err)

data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
names = ['A', 'B', 'C']

df = generate_df(data, names)
print("DataFrame:")
print(df)