
# University Scholarship Allocation System

MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARK = 50.0
MIN_ATTENDANCE = 75.0
MAX_INCOME = 250000

students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nEnter details for student {i + 1}")

    name = input("Student name: ")
    aggregate = float(input("Aggregate marks (%): "))
    min_subject = float(input("Lowest subject mark (%): "))
    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs.): "))

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if min_subject < MIN_SUBJECT_MARK:
        reasons.append("Subject mark below 50%")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Income exceeds Rs. 2,50,000")

    students.append({
        "name": name,
        "aggregate": aggregate,
        "min_subject": min_subject,
        "attendance": attendance,
        "income": income,
        "eligible": len(reasons) == 0,
        "reasons": reasons
    })

# Select eligible students
eligible = [s for s in students if s["eligible"]]
ineligible = [s for s in students if not s["eligible"]]

# Ranking and tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Higher minimum subject mark
# 5. Alphabetical order of name

eligible.sort(key=lambda s: (
    -s["aggregate"],
    -s["attendance"],
    s["income"],
    -s["min_subject"],
    s["name"].casefold()
))

print("\n===== SCHOLARSHIP RANK LIST =====")

if eligible:
    for rank, student in enumerate(eligible, start=1):
        print(
            f"{rank}. {student['name']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']:.2f}% | "
            f"Income: Rs. {student['income']:.2f}"
        )
else:
    print("No eligible students.")

print("\n===== INELIGIBLE STUDENTS =====")

if ineligible:
    for student in ineligible:
        print(f"{student['name']}: " + ", ".join(student["reasons"]))
else:
    print("All applicants are eligible.")

