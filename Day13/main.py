############DEBUGGING#####################
from random import randint


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5)
print(dice_imgs[dice_num])

year = int(input("What's your year of birth?"))
if 1980 < year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
