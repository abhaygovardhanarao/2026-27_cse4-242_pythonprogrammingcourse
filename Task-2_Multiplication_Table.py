# Write a Python program to print the multiplication table of a number
number = int(input("Enter a number: "))

print(f"\n--- Multiplication Table of {number} (Using For Loop) ---")
for i in range(1, 11):
  product = number * i
  print(f"{number} x {i} = {product}")

print(f"\n--- Multiplication Table of {number} (Using While Loop) ---")
j = 1
while j <= 10:
  product = number * j
  print(f"{number} x {j} = {product}")
  j += 1