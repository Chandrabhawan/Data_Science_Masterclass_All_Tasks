# PY200_T3 — Electricity Bill Calculation
# Author  : Chandra Patel

# Input units
units = int(input("Enter electricity units: "))

bill = 0

# Slab 1: First 100 units
if units > 0:
    if units <= 100:
        bill = units * 2
    else:
        bill = 100 * 2

# Slab 2: Next 100 units (101–200)
if units > 100:
    if units <= 200:
        bill = bill + (units - 100) * 3
    else:
        bill = bill + 100 * 3

# Slab 3: Next 300 units (201–500)
if units > 200:
    if units <= 500:
        bill = bill + (units - 200) * 5
    else:
        bill = bill + 300 * 5

# Slab 4: Above 500 units
if units > 500:
    bill = bill + (units - 500) * 8

# Add fixed charge
if units > 0:
    bill = bill + 50

# Output result
print("Total Electricity Bill =", bill)