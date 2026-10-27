# 1. University Scholarship Allocation System

## 1. Problem Statement

The University Scholarship Allocation System is designed to evaluate students based on their academic performance, subject-wise minimum marks, attendance percentage, and annual family income.

The system checks whether each student satisfies all eligibility criteria. Eligible students are ranked according to their aggregate marks. If two or more students have the same aggregate marks, ties are resolved using the following rules:

1. Higher attendance percentage.
2. Lower annual family income.
3. Higher minimum subject mark.
4. Student name in alphabetical order.

The system displays the eligible students in rank order and identifies students who are not eligible along with their reasons.

## 2. Algorithm

1. Start the program.
2. Read the scholarship eligibility criteria.
3. Enter the number of applicants.
4. For each student, input their name, aggregate marks, minimum subject mark, attendance percentage, and annual family income.
5. Check the eligibility criteria:
   - Aggregate marks must be at least 75%.
   - Every subject must meet the minimum requirement of 50%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
6. Separate eligible and ineligible students.
7. Sort eligible students using the predefined ranking and tie-breaking rules.
8. Display the eligible students with their ranks.
9. Display the ineligible students and their rejection reasons.
10. Stop the program.

## 3. Flowchart



## 5. Sample Input

The following example uses four applicants.

```
Enter number of applicants: 4

Enter details for student 1
Student name: Arun
Aggregate marks (%): 90
Lowest subject mark (%): 65
Attendance (%): 90
Annual family income (Rs.): 200000

Enter details for student 2
Student name: Bala
Aggregate marks (%): 90
Lowest subject mark (%): 70
Attendance (%): 90
Annual family income (Rs.): 180000

Enter details for student 3
Student name: Chitra
Aggregate marks (%): 72
Lowest subject mark (%): 60
Attendance (%): 80
Annual family income (Rs.): 150000

Enter details for student 4
Student name: Divya
Aggregate marks (%): 85
Lowest subject mark (%): 45
Attendance (%): 95
Annual family income (Rs.): 100000
```

## 6. Sample Output

```
===== SCHOLARSHIP RANK LIST =====
1. Bala | Aggregate: 90.00% | Attendance: 90.00% | Income: Rs. 180000.00
2. Arun | Aggregate: 90.00% | Attendance: 90.00% | Income: Rs. 200000.00

===== INELIGIBLE STUDENTS =====
Chitra: Aggregate below 75%
Divya: Subject mark below 50%
```
