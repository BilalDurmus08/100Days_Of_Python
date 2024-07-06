line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map1 = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "B3"  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0]
number = int(position[1])
letterNumber = 0

number = number - 1
if letter == "A":
    letterNumber = 0
elif letter == "B":
    letterNumber = 1
else:
    letterNumber = 2

map1[number][letterNumber] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
