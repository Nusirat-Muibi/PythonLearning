student = {
    "name": "Nushirot",
    "age": 29,
    "grade": "A"
}

print(student["name"])
print(student["age"])
print(student["grade"])

student["subject"] = "python"
print(student)

student["age"] = 21
print(student["age"])

del student["grade"]
print(student)

for key, value in student.items():
    print(key, ":", value)
