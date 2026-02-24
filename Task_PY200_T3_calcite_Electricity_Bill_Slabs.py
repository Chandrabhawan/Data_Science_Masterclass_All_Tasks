# PY200_T3 — Electricity Bill Calculation
# Author  : Chandra Patel

units = int(input("Enter electricity units consumed: "))

bill = 0

if units > 0:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
    elif units <= 500:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    else:
        bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 8)

    bill += 50  # Fixed charge

print(f"\n--- Electricity Bill ---")
print(f"Units Consumed : {units}")
print(f"Total Bill     : ₹{bill}")