"""11. Given the sales information of a company as CSV file with the following fields
month_number, facecream, facewash, toothpaste, bathingsoap, shampoo,
moisturizer, total_units, total_profit. Write Python codes to visualize the data as follows"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file):
    return pd.read_csv(file)

def scatter_plot(df):
    plt.scatter(df['month_number'], df['toothpaste'], color='blue')
    plt.xlabel('Month')
    plt.ylabel('Toothpaste Sales')
    plt.title('Toothpaste Sales per Month')
    plt.show()

def bar_chart(df):
    df[['facecream', 'facewash']].plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Face Cream and Face Wash Sales')
    plt.show()

def pie_chart(df):
    total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
    total_sales.plot.pie(autopct='%1.1f%%')
    plt.title('Total Sales Distribution')
    plt.ylabel('')
    plt.show()

data_file = "sales.csv"
data = load_data(data_file)
scatter_plot(data)
bar_chart(data)
pie_chart(data)