#student score tracker

name = input("Enter student name:")
subject =input("Enter student subject:")
score = input("Enter student score:")
grade = input("Enter student grade:")
teacher_name = input("Enter Teacher name:")

user_input ={
    "Name": name,
    "Subject": subject,
    "Score": score,
    "Grade": grade,
    "Teacher_name": teacher_name
}
for i, j in user_input.items():
    print(f"{i} : {j}")

