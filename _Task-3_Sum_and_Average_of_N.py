# Write a Python program to find the sum and average of N numbers using for loop
n = int(input("Enter how many numbers you want to enter (N): "))

total_sum = 0

if n > 0:
  for i in range(1, n + 1):
    num = float(input(f"Enter number {i}: "))
    total_sum += num

  # Calculate average
  average = total_sum / n

  print("\n--- Results ---")
  print(f"Sum of the {n} numbers = {total_sum}")
  print(f"Average of the {n} numbers = {average:.2f}")
else:
  print("Please enter a valid positive integer for N.")