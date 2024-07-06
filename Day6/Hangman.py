import random
import words

word_picker = random.choice(words.word_list)
word_look = []

for letter in range(0, len(word_picker)):
    word_look += '_'

print(word_look)
print(word_picker)
hangmanLife = 0
end_of_the_game = False


def is_include(word, letter1):
    is_true = False
    for x in range(0, len(word)):
        if word[x] == letter1:
            is_true = True

    return is_true


while hangmanLife < 7:
    end_of_the_game = True
    letter_guess = input("Guess a letter: ")
    if is_include(word_picker, letter_guess):
        for number in range(0, len(word_picker)):
            if word_picker[number] == letter_guess:
                word_look[number] = letter_guess
                print(word_look)

    else:
        hangmanLife += 1
        print(f"Remaining life {7 - hangmanLife}")

    for letter1 in word_look:
        if letter1 == '_':
            end_of_the_game = False

    if end_of_the_game:
        break


