#this let us inside of loop count the index

list1 = [5, 8, 9, 11]
for i, value in enumerate(list1):
    print(f"The index: {i}, The value: {value}")


#loops
number = 0
while number < 5:
    #break stop the loop
    #continue stop the rest of this iteration. And make it start beginning of loop
    number += 1
    if number == 3:
        continue
    print(number)


for x in range(2):
    pass
    #If we want to create a loop and wants to fill that loop after a while. We can use pass


print("Done")

