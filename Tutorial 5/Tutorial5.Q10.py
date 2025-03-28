"""10. Create a stud.csv file containing rollno, name, place and mark of students. Use this file and do the following"""

import pandas as pd
import matplotlib.pyplot as plt

f_name = "stud.csv"

def load(f_name):
    return pd.read_csv(f_name)

def set_idx(df):
    return df.set_index('rollno')

def get_nm_mk(df):
    return df[['name', 'mark']]

def sort_nm(df):
    return df.sort_values(by='name')[['rollno', 'name', 'mark']]

def sort_mk_desc(df):
    return df.sort_values(by='mark', ascending=False)[['rollno', 'name', 'mark']]

def stats(df):
    return {
        "Avg": df['mark'].mean(),
        "Med": df['mark'].median(),
        "Mode": df['mark'].mode()[0]
    }

def min_max(df):
    return df['mark'].min(), df['mark'].max()

def var_std(df):
    return df['mark'].var(), df['mark'].std()

def plot_hist(df):
    df['mark'].hist()
    plt.xlabel("Marks")
    plt.ylabel("Freq")
    plt.title("Histogram of Marks")
    plt.show()

def drop_plc(df):
    return df.drop(columns=['place'])

data = load(f_name)
print("Original Data:")
print(data)
print("\nData with Roll Number as Index:")
print(set_idx(data))
print("\nName and Mark Columns:")
print(get_nm_mk(data))
print("\nSorted by Name:")
print(sort_nm(data))
print("\nSorted by Mark (Descending):")
print(sort_mk_desc(data))
print("\nStatistics:")
print(stats(data))
print("\nMinimum and Maximum Marks:")
print(min_max(data))
print("\nVariance and Standard Deviation:")
print(var_std(data))
print("\nHistogram:")
plot_hist(data)
print("\nData without Place Column:")
