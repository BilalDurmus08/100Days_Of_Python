#The sets are contain only unique items
my_sets = {5, 7, 8, 11, 55, 55}

print(my_sets)  #it won't print same item two times
#in sets there is np o index like dictionary


#Truth and Falsy
something = "apple" #for boolean TRUE
something1 = ""     #for boolean FALSE
something2 = 0      #for boolean FALSE
something3 = 20     #for boolean TRUE

print(f"{bool(something)}\n{bool(something1)}\n{bool(something2)}\n{bool(something3)}")


#Ternary Operator

is_true = True

print("This statement is True") if is_true else print("This statement is false")

# == checks are they same object.  (is) checks that are they in same place memory.
print([1, 2, 3] is [1, 2, 3])  #false
print([1, 2, 3] == [1, 2, 3])  #True




