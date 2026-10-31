# Write a python program to find the largest number in a series of N numbers entered by the user using for loop
n = int(input("Enter how many numbers you want to enter (N): "))
if n > 0:
  # Read the first number to initialize the largest variable
  first_num = float(input("Enter number 1: "))
  largest = first_num

  # Loop for the remaining N-1 numbers
  for i in range(1, n):
    num = float(input(f"Enter number {i + 1}: "))
    if num > largest:
      largest = num
  print("\n--- Results ---")
  print(f"The largest number among the {n} entered numbers is: {largest}")
else:
  print("Please enter a valid positive integer for N.")