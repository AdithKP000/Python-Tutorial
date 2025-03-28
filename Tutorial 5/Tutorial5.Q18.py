""" 18. Consider a CSV file 'weather.csv' with the following columns (date, temperature, humidity, windSpeed, precipitationType, place, weather {Rainy, Cloudy, Sunny}).
Write commands to do the following using Pandas library:

1. Print first 10 rows of weather data.
2. Find the maximum and minimum temperature.
3. List the places with temperature less than 28°C.
4. List the places with weather = "Cloudy".
5. Sort and display each weather and its frequency.
6. Create a bar plot to visualize temperature of each day.
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


weather_data = pd.read_csv("weather.csv")

print("First 10 rows of weather data:")
print(weather_data.head(10))

max_temp = weather_data["temperature"].max()
min_temp = weather_data["temperature"].min()
print("\nMaximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
low_temp_places = weather_data[weather_data["temperature"] < 28]["place"].unique()
print("\nPlaces with temperature less than 28°C:", low_temp_places)

cloudy_places = weather_data[weather_data["weather"] == "Cloudy"]["place"].unique()
print("\nPlaces with Cloudy weather:", cloudy_places)

weather_frequency = weather_data["weather"].value_counts()
print("\nWeather Frequency:")
print(weather_frequency)

plt.figure(figsize=(10,5))
plt.bar(weather_data["date"], weather_data["temperature"], color='blue')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature of Each Day")
plt.xticks(rotation=45)
plt.show()