

def addiction(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


operations = {
    "+": addiction,
    "-": subtraction,
    "/": divide,
    "*": multiply,
}
is_the_end = "Y"

num1 = int(input("Give the first number: "))
while is_the_end == "Y":

    num2 = int(input("give the second number: "))
    for operator1 in operations:
        print(operator1)

    operator = str(input("Select an operator: "))
    operator_function = operations[operator]

    num1 = operator_function(num1, num2)

    print(num1)
    is_the_end = str(input("Wanna continue Y or N: "))