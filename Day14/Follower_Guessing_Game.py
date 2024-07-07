import Data
import random
import art

isTrue = True
correct_number = 0
while isTrue:
    print(f"\nCorrect question number: {correct_number}\n")
    ques1 = random.choice(Data.data)
    ques2 = random.choice(Data.data)

    print(f"Compare A: {ques1['name']}, {ques1['description']}, {ques1['country']}")

    print(art.vs)

    print(f"Compare B: {ques2['name']}, {ques2['description']}, {ques2['country']} ")

    answer = input("Which one has more million follower A or B: ")

    if ques1['follower_count'] > ques2['follower_count']:
        max_follower = 'A'
    else:
        max_follower = 'B'

    if answer == max_follower:
        correct_number += 1
    else:
        break

print(f"You lost. The total correct answer is: {correct_number}")



