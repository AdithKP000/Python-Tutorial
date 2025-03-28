"""5.Read data from an excel file."""

import pandas as pd

data = pd.read_excel("output.xlsx", index_col=0)
print("Data read from output.xlsx:")
print(data)
