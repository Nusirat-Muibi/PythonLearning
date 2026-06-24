score = 0

print("Question 1:")
answer1 = input("What is the capital of Nigeria? ")
if answer1.lower() == "abuja":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is abuja.")

print("Question 2:")
answer2 = input("what is 10 * 3? ")
if answer2 == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 30.")
print("Question 3:")
answer3 = input("What colour is the Nigeria flag? ")
if answer3.lower() == "green":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is green.")
print("Your score is", score, "out of 3")

