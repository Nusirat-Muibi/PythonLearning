'''def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"'''


'''def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")
print(check_even_odd(15))'''

def check_even_odd(number):
    remainder = number % 2
    if remainder == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")
        print("Reminder:",remainder)


print(check_even_odd(20))
