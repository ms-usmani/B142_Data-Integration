#!/usr/bin/env python3
import sys

current_store = None
total_sales = 0
num_sales = 0

for line in sys.stdin:
    store, sales = line.strip().split('\t')
    sales = float(sales)

    if current_store == store:
        total_sales += sales
        num_sales += 1
    else:
        if current_store:
            average_sales = total_sales / num_sales
            print(f"{current_store}\t{average_sales}")
        current_store = store
        total_sales = sales
        num_sales = 1

# Output the last store's average sales
if current_store == store:
    average_sales = total_sales / num_sales
    print(f"{current_store}\t{average_sales}")
