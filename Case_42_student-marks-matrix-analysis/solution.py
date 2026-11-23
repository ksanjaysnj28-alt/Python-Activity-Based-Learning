# Case Study 42: Student Marks Matrix Analysis
# Marks are stored as a nested list: each row belongs to one student.

students = ["Asha", "Bharat", "Charan", "Diya"]
subjects = ["Python", "Maths", "Statistics"]
marks = [
    [86, 78, 91],
    [72, 81, 69],
    [94, 88, 90],
    [58, 65, 62]
]
low_average_limit = 60

print("STUDENT-WISE RESULTS")
highest_total = -1
topper = ""

for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):
        total = total + marks[i][j]
    average = total / len(subjects)
    print(students[i], "Total:", total, "Average:", round(average, 2))
    if total > highest_total:
        highest_total = total
        topper = students[i]

print("\nSUBJECT-WISE AVERAGES")
for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(students)):
        subject_total = subject_total + marks[i][j]
    subject_average = subject_total / len(students)
    print(subjects[j], "Average:", round(subject_average, 2))
    if subject_average < low_average_limit:
        print("Warning: low average in", subjects[j])

print("\nTop performer:", topper, "with", highest_total, "marks")
