import random

input_level = 0
level = input("How hard do you want: Easy or Hard: ").lower()

if level == "easy":
    input_level = 5
elif level == "hard":
    input_level = 10

number = random.randint(0, 100)

while True:
    print(f"Remaining life: {input_level}")
    guess = int(input("Guess a number: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    elif guess == number:
        print("You guessed right !!!")
        break
    input_level -= 1
    if input_level == 0:
        print("Out of life ?!")
        break

