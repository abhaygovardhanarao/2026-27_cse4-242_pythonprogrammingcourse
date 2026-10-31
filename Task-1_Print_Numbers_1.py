# Write a Python program to print numbers from 1 to N
n = int(input("Enter the value of N: "))
print("\n--- Using For Loop ---")
for i in range(1, n + 1):
  print(i, end=" ")
print()  # New line after loop completion
print("\n--- Using While Loop ---")
j = 1
while j <= n:
  print(j, end=" ")
  j += 1
print()