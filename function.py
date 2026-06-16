def check_grade(scores):
    if scores >= 92:
        print("Excellent")
    elif scores >= 85:
        print("Good")
    elif scores >= 60:
        print("Average")
    else:
        print("Failing")
    print(scores)


scores = int(input("Enter your score: "))

check_grade(scores)