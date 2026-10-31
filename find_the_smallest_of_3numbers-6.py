# A python program to find the smallest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare numbers using nested if-else statements
if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

# Output the result
print(f"The smallest number is:",smallest)