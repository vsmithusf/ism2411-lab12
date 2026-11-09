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
    next(reader) # skip header
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
high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f: # write mode, newline="" to avoid extra blank lines on Windows
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)
print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

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
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
            product = row["product"]
            total = float(row["price"]) * int(row["quantity"])
            summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print(" ")
print("--- Exercise 8: Append Mode Log ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")
# Reflection 1: Python allows you to quickly and efficiently read and add values from a list together, while providing you flexibility
# to add additional fields with ease, something that Excel doesn't allow you to do as easily. Python also allows you to count timestamps,
# which is something Excel is not capable of doing. However, Excel is easier to read and provides many more options than Python does
# regarding readability of a dataset, while still allowing you to perform calculations across an entire dataset like Python.
# Reflection 2: Logging when an employee enters a dataset to add values is a great example of when an append-mode log file would be
# useful, and it is useful here because it allows you to add an unlimited amount of values to a list or dictionary with dedicated
# timestamps through the datatime function.