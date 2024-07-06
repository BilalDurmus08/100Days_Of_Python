import random  #In this project I have created an random password creator.
import string

symbols = "!@#$%^&*()_+-=[]{}|;':,./<>?"
numbers = "0123456789"


letterNumber = int(input("How many letters would you like in your password?\n"))
symbolNumber = int(input(f"How many symbols would you like?\n"))
numberNumber = int(input(f"How many numbers would you like?\n"))

lowercase_alphabet = string.ascii_lowercase
alphabetNumber = letterNumber - symbolNumber - numberNumber
passwordBefore = ""

for letter in range(0, alphabetNumber):
    passwordBefore += random.choice(lowercase_alphabet)

for symbol in range(0, symbolNumber):
    passwordBefore += random.choice(symbols)

for number in range(0, numberNumber):
    passwordBefore += random.choice(numbers)

charList = list(passwordBefore)

random.shuffle(charList)

password = "".join(charList)

print(password)
