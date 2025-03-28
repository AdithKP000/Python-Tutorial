"""9. Reading the data file and showing the first five records"""

import pandas as pd

def clean_update_csv(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.to_csv(file_path, index=False)
    return df

def most_expensive_car(df):
    return df.loc[df['price'].idxmax(), 'company']

def toyota_cars(df):
    return df[df['company'].str.lower() == 'toyota']

def total_cars_by_company(df):
    return df['company'].value_counts()

def highest_priced_car(df):
    return df.loc[df['price'].idxmax()]

def avg_mileage_by_company(df):
    return df.groupby('company')['average-mileage'].mean()

def sort_by_price(df):
    return df.sort_values(by='price')

def first_five_records(df):
    return df.head()

file_path = "auto.csv"
data = clean_update_csv(file_path)
print("Most Expensive Car Company:", most_expensive_car(data))
print("Toyota Cars:\n", toyota_cars(data))
print("Total Cars by Company:\n", total_cars_by_company(data))
print("Highest Priced Car:\n", highest_priced_car(data))
print("Average Mileage by Company:\n", avg_mileage_by_company(data))
print("Cars Sorted by Price:\n", sort_by_price(data))
print("First Five Records:\n", first_five_records(data))
