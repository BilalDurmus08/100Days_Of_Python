import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Continues = input("Wanna play Black Jack y or n: ").lower()


while Continues == "y":

    myCards = []
    computerCards = []

    myCards.append(random.choice(cards))
    myCards.append(random.choice(cards))
    print(f"Here your cards: {myCards}")

    computerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))
    print(f"The opponent's first card is: {computerCards[0]}")

    choice = input("Wanna hit or stay: ").lower()
    while choice == "hit":
        if choice == "hit":
            myCards.append(random.choice(cards))
            print(f"Here your cards: {myCards}")
        choice = input("Wanna hit or stay: ").lower()
    print("asdfasdfa")

    number = random.randint(0, 1)
    while sum(computerCards) < 17 or number == 0:
        computerCards.append(random.choice(cards))
        number = random.randint(0, 4)

    print(f"\nHere Computer's Cards: {computerCards}")

    if sum(myCards) > 21:
        print("The computer wins :/")
    elif sum(computerCards) > 21:
        print("I won YEEYY!!!!")
    elif 21 - sum(myCards) == 21 - sum(computerCards):
        print("It is a Draw!!")
    elif 21 - sum(myCards) < 21 - sum(computerCards):
        print("I won YEEYY!!!!")
    elif 21 - sum(myCards) > 21 - sum(computerCards):
        print("The computer wins :/")
    else:
        print("I do not know why this printed ?")

    Continues = input("\nWanna play Black Jack y or n: ").lower()







