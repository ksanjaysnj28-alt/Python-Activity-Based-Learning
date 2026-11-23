# Case Study 66: Student Academic Risk Classification

students = ["Aarav", "Bhavna", "Chirag", "Divya", "Eshan"]
marks = [72, 45, 38, 81, 55]
attendance = [88, 82, 62, 70, 78]
lab_scores = [76, 42, 35, 86, 61]

low_count = 0
moderate_count = 0
high_count = 0
print("STUDENT ACADEMIC RISK REPORT")

for i in range(len(students)):
    risk_factors = 0
    reasons = []

    if marks[i] < 50:
        risk_factors = risk_factors + 1
        reasons.append("Low marks")
    if attendance[i] < 75:
        risk_factors = risk_factors + 1
        reasons.append("Low attendance")
    if lab_scores[i] < 50:
        risk_factors = risk_factors + 1
        reasons.append("Low lab score")

    if risk_factors >= 2:
        category = "HIGH"
        high_count = high_count + 1
    elif risk_factors == 1:
        category = "MODERATE"
        moderate_count = moderate_count + 1
    else:
        category = "LOW"
        low_count = low_count + 1

    print(students[i], "Risk factors:", risk_factors, "Category:", category)
    if risk_factors > 0:
        print("  Reasons:", ", ".join(reasons))

print("\nCATEGORY SUMMARY")
print("LOW:", low_count, "MODERATE:", moderate_count, "HIGH:", high_count)
