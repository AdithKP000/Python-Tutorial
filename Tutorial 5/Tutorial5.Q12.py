"""12. How to plot two or more lines on a same plot with suitable legends, labels and title."""

import matplotlib.pyplot as plt
import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def multi_line_plot(df):
    plt.plot(df['month_number'], df['facecream'], marker='o', label='Face Cream')
    plt.plot(df['month_number'], df['facewash'], marker='s', label='Face Wash')
    plt.plot(df['month_number'], df['toothpaste'], marker='^', label='Toothpaste')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Sales Trends Over Time')
    plt.legend()
    plt.show()

data_file = "sales.csv"
data = load_data(data_file)
multi_line_plot(data)
