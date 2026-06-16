#student grade checker

def check_grade(name,score):

    if score >= 90:
        return f"{name}:A"
    elif score >= 80:
        return f" {name}:B"
    elif score >= 70:
        return f" {name}:C"
    elif score >= 60:
        return f" {name}:D"
    else:
        return f"{name}:F"
print( check_grade("Nushirot" ,92))
print( check_grade("Tomisin" , 85))
print( check_grade("Tomisin", 73))
print( check_grade("Sara" , 60))
print( check_grade("John" , 45))




