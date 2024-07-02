#!/usr/bin/env python

import sys

def mapper():
    for line in sys.stdin:
        # Split the line into columns
        data = line.strip().split(',')
        if data[0] != 'Store':  # Skip header
            store = data[0]
            try:
                weekly_sales = float(data[3])  # Weekly_Sales column
                print(f"{store}\t{weekly_sales}")
            except ValueError:
                continue

if __name__ == "__main__":
    mapper()
