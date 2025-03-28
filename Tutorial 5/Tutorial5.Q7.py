"""7. Create a data frame from the dictionary of lists."""

import pandas as pd

data_info = {
    "SN": [1, 2, 3],
    "Name": ["Linus Torvalds", "Tim Berners-Lee", "Guido van Rossum"],
    "Country": ["Finland", "England", "Netherlands"],
    "Contribution": ["Linux Kernel", "World Wide Web", "Python"],
    "Year": [1991, 1990, 1991]
}

df = pd.DataFrame(data_info)
print(df)
