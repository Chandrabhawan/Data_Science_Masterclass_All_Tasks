# PY200_T4 — Password Strength Checker
# Author  : Chandra Patel

# Take input
password = input("Enter your password: ")

# Initialize conditions
has_digit = False
has_upper = False
has_lower = False

# Check each character manually
for ch in password:
    if ch >= '0' and ch <= '9':
        has_digit = True
    elif ch >= 'A' and ch <= 'Z':
        has_upper = True
    elif ch >= 'a' and ch <= 'z':
        has_lower = True

# Check all conditions
if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("STRONG")
else:
    print("WEAK")