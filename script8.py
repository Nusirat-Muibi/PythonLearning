students = {
    "student1" : {
        "name" : "Nushirot",
        "age" : 21,
        "grade" : "A"
    },
    "student2" : {
        "name" : "Damilare",
        "age" : 20,
        "grade" : "B"
    }
}
print(students["student1"]["name"])
print(students["student2"]["grade"])
students["student1"] ["age"] = 21
print(students["student1"] ["age"])
students["student1"] ["subject"] ="python"
print(students["student1"])

for student,info  in students.items():
    print(student)
    for key,value in info.items():
        print(key, ":",  value)




