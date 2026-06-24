import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct!")
elif guess < number:
    print("Too low!")
else:
    print("Too high!")


import random
number = random.randint(1, 10)
guesses = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses +=1
    if guess == number:
        print("Correct! You get it in" , guesses, "guesses!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")




