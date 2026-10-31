marks = float(input("Enter student's marks: "))
if marks >=90:
    grade = 'A'
elif marks >=80:
    grade = 'B'
elif marks >=70:
    grade = 'C'
else:
    grade = 'D'
print(f"Grade: {grade}")