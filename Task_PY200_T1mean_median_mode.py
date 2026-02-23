# Task_PY200_T1 — Mean, Median, and Mode using first principle (Basic constructs, not using function, or inbuilt functions)
# Author  : Chandra Patel

# Input array/Data
arr = [2, 4, 6, 2, 8, 4, 2]

# ------------------ MEAN ------------------
total = 0
count = 0

for num in arr:
    total = total + num
    count = count + 1

mean = total / count
print("Mean:", mean)


# ------------------ MEDIAN ------------------

# Step 1: Sort array manually (Bubble Sort)
n = len(arr)
sorted_arr = arr.copy()

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_arr[j] > sorted_arr[j + 1]:
            temp = sorted_arr[j]
            sorted_arr[j] = sorted_arr[j + 1]
            sorted_arr[j + 1] = temp

# Step 2: Find median
if n % 2 == 1:
    median = sorted_arr[n // 2]
else:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

print("Median:", median)


# ------------------ MODE ------------------
max_count = 0
mode = None

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1

    if count > max_count:
        max_count = count
        mode = arr[i]

print("Mode:", mode)
