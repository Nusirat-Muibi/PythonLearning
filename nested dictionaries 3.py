#Employee Record

employees = {
    "employee1" : {
        "name" : "Ali",
        "department" : "IT",
        "salary" : 50000
},
    "employee2" : {
        "name" : "Sara",
        "department" : "HR",
        "salary": 45000
    }
}
print(employees["employee1"] ["department"])
print(employees["employee2"] ["salary"])
employees["employee1"] ["salary"] = 55000
print(employees["employee1"])
employees["employee2"] ["experience"] = 3

for employee, info in employees.items():
    print(employee)
    for key,value in info.items():
        print(key, ":", value)
