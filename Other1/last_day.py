#fin duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = some_list.copy()
for x in some_list:
    new_list.remove(x)
    if x in new_list:
        print("Copies", x)


#Args parameters and kwargs

def super_func(*args, **kwargs):
    print(kwargs)  #{'number1': 1, 'number2': 5}
    return sum(args)


print(super_func(5, 8, 8, 9, 4, 11, number1=1, number2=5))


#Dependency Injections
#bringing the global value inside a function
total_number = 0


def total(number):
    return number + 1


print(total(total(total_number)))


#Map, Filter, Zip and Reduce
#Maps are PURE functions
my_list = [1, 2, 3]
my_list1 = [10, 20, 30]

def doubled(number):
    return number*2


def only_odd(number):
    return number % 2 == 0


print(f"Original list: {my_list}")

#Map function
function_map = list(map(doubled, my_list))
print(function_map)

#Filterr function
function_filter = list(filter(only_odd, my_list))
print(function_filter)

#Zip function
function_zipped = list(zip(my_list1, my_list))
print(function_zipped)
