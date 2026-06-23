try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by Zero.")
except ValueError:
    print("Error: please enter valid number.")


items = {
    "rice": 5000,
    "sugar": 3000,
    "oil": 4500,
    "flour": 2000,
    "milk": 1500
}
item = input("Enter items name: "). lower()
try:
    price = items[item]
    print(f"The price of {item} is {price}")
except KeyError:
    print("Sorry,that item is not in the store!")

