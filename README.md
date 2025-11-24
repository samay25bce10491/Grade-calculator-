1.Students face a lot of difficulties when calculating their grades manually based on marks from different subjects.
A grade calculator automates this process by taking marks as input and calculating:
Total marks
Percentage
Grade (A/B/C/Fail)
Pass/Fail status
This helps reduce human error and saves time.
2. Analyzing the Requirements
Functional Requirements
User enters the marks for several subjects
Calculate total marks
Calculate percentage
Determine grade
Display results
Non-Functional Requirements
Simple and user-friendly
Fast calculations
Works for any valid numerical input
3. Top-down Design
Main Program →
Input Module → Get subject marks
* Processing Module → Calculate total & percentage
* Grade Module → Determine grade
* Output Module → Display results
4. Development of Algorithm
Algorithm for Grade Calculator
1. Begin
2. Input marks of all subjects
3. Sum all marks to get total
4. Calculate percentage = (total / max_marks) × 100
5. If the percentage ≥ 90 → Grade A
6. Else if ≥ 75 → Grade B
7. Else if ≥ 50 → Grade C
8. Else → Fail
9. Display total, percentage, and grade
10. Conclusion
# Grade-calculator-
python program 
