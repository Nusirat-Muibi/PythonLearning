file = open("test.txt" , "w")
file.write("Hello, welcome to file handling!")
file.close()

file = open("test.txt", "a")
file.write("\n This is new line!")
file.close()

with open("test.txt" , "r") as file:
    print(file.read())

sales = [
    ("Rice", 5000),
    ("Sugar", 3000),
    ("Oil", 4500),
    ("Flour", 2000),
    ("Milk", 1500)
]
with open("sales.txt", "w") as file:
    for items, amount in sales:
        file.write(f"{items}: {amount}\n")
with open("sales.txt", "a") as file:
        file.write("Bread: 2500\n")

with open("sales.txt", "r") as file:
    print(file.read())

