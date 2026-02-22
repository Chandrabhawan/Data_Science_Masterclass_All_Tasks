# PY200_T2 — Check if a Number is Positive, Negative, or Zero
# Author  : Chandra Patel

# Take input from user
num = float(input("Enter a number: "))

# Check condition
if num > 0:
    print(f"Your entered number {num} is positive.")

elif num < 0:
    positive_value = num * -1
    print(f"Your entered number {num} was negative, however positive value of your number is {positive_value}.")

else:
    print(f"Your entered number {num} is zero.")