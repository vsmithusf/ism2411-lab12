# csv_practice.py
# Author: Van Smith
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("--- Exercise 1: Get the File ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print(" ")
print("--- Exercise 2: Read and Print Raw Rows ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print(" ")
print("--- Exercise 3: Skip the Header ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader) # next() returns the next item from the iterator, which is the header row in this
    print(f"Header: {header}")
    for row in reader:
        print(row)

print(" ")
print("--- Exercise 4: Compute Totals ---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

print(" ")
print("--- Exercise 5: Filter and Write ---")


print(" ")
print("--- Exercise 6: csv.DictReader ---")
dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total Revenue: ${dict_total:.2f}")

print(" ")
print("--- Exercise 7: Sales Summary by Product ---")


print(" ")
print("--- Exercise 8: Append Mode Log ---")



# Reflection 1:
# Reflection 2: