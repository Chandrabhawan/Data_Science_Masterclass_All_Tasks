# PY200_T6 — Smallest Number with Digit Constraints
# Author  : Chandra Patel

# Input
n = int(input("Enter N: "))

found = -1

# Loop from 1 to N
for x in range(1, n + 1):

    num = x
    digit_sum = 0
    count_3   = 0
    has_zero  = 0

    # Extract digits manually using % and //
    while num > 0:
        digit = num % 10

        # Sum of digits
        digit_sum = digit_sum + digit

        # Count how many 3s
        if digit == 3:
            count_3 = count_3 + 1

        # Check if zero exists
        if digit == 0:
            has_zero = 1

        num = num // 10

    # Check all 3 conditions
    if digit_sum % 7 == 0 and count_3 == 2 and has_zero == 0:
        found = x
        break  # Smallest found → stop

# Output
if found != -1:
    print("Smallest number found :", found)
else:
    print("No such number found. Result : -1")