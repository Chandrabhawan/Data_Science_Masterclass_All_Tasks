# PY200_T4 — Password Strength Checker
# Author  : Chandra Patel

password = input("Enter your password: ")

# ─────────────────────────────────────────────
# CHECK 1: Length >= 8
# ─────────────────────────────────────────────
length = 0
for char in password:
    length = length + 1

has_length = length >= 8

# ─────────────────────────────────────────────
# CHECK 2: At least 1 digit
# ─────────────────────────────────────────────
has_digit = False
for char in password:
    if char >= "0" and char <= "9":
        has_digit = True

# ─────────────────────────────────────────────
# CHECK 3: At least 1 uppercase
# ─────────────────────────────────────────────
has_upper = False
for char in password:
    if char >= "A" and char <= "Z":
        has_upper = True

# ─────────────────────────────────────────────
# CHECK 4: At least 1 lowercase
# ─────────────────────────────────────────────
has_lower = False
for char in password:
    if char >= "a" and char <= "z":
        has_lower = True

# ─────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────
print()
print(f"Password          : {password}")
print(f"Length >= 8       : {has_length}  (length = {length})")
print(f"Has digit         : {has_digit}")
print(f"Has uppercase     : {has_upper}")
print(f"Has lowercase     : {has_lower}")
print()

if has_length and has_digit and has_upper and has_lower:
    print("Result : STRONG ✅ — Valid Password")
else:
    print("Result : WEAK ❌ — Invalid Password")

    # Tell user exactly what is missing
    if not has_length:
        print(f"  → Need at least 8 characters (you have {length})")
    if not has_digit:
        print("  → Need at least 1 digit (0–9)")
    if not has_upper:
        print("  → Need at least 1 uppercase letter (A–Z)")
    if not has_lower:
        print("  → Need at least 1 lowercase letter (a–z)")