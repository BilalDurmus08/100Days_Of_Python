
bets = {}

answer = "yes"

while answer == "yes":
    person = input("Who will give a bet: ")
    amount = int(input("How much will you bet: "))
    bets[person] = amount
    answer = input("Are there any other person? Yes or No: ").lower()

max_bet = 0
max_person = ""
for key in bets:
    if bets[key] > max_bet:
        max_bet = bets[key]
        max_person = key

print(f"{max_person} gave the max bet. The bet is: {max_bet}")