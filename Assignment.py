def check_grade(score):
 if score >= 90:
     return "Excellent"
 elif score >= 75:
       return "Good"
 elif score >= 60:
       return "Average"
 else:
    return "Failing"
scores = [85, 92, 55, 73, 60]
for score in scores:
    grade = check_grade(score)
    print("Score:", score,  "Grade:", grade)