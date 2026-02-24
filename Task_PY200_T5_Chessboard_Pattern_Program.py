# PY200_T5 — Chessboard Pattern Program
# Author  : Chandra Patel

# Input size
n = int(input("Enter value of N: "))

# Loop through rows
for i in range(1, n + 1):
    
    # Loop through columns
    for j in range(1, n + 1):
        
        # Check diagonal condition first
        if i == j:
            print("X", end=" ")
        
        # Check even/odd condition
        elif (i + j) % 2 == 0:
            print("1", end=" ")
        
        else:
            print("0", end=" ")
    
    # Move to next line after each row
    print()