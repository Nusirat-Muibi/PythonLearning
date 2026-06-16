def my_function():
    return ["apple", "banana", "cherry", "mango", "grape"]
fruits = my_function()
print (len(fruits))
fruits.append ("watermelon")
fruits.remove ("banana")
fruits.sort()
print(fruits)
print(fruits[0:3])
print("mango" in fruits)
for fruit in fruits:
    print(fruit.upper())