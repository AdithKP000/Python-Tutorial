"""""6. Write Python program to write the data given below to a CSV file."""

import csv

def save_to_csv(filename, records):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(records)
    print(f"Data written to {filename}")

data_entries = [
    ["SN", "Name", "Country", "Contribution", "Year"],
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

save_to_csv("contributors.csv", data_entries)   