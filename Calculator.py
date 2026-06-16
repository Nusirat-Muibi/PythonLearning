num1 = float(input("Enter first number:"))
op = input("Enter operation(+, -, /, *): ")
num2 = float(input("Enter second number:"))
total = 0
if op == "+":
    total = num1 + num2
    print(f"this is the total:{total}")
elif op == "-":
    print(num1-num2)
    if total > 8:
        print("no is not greater than 8")
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Fail you can't divide by zero")
else:
    print("invalid operation")