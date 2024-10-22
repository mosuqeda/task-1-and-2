def addition(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def times(num1, num2):
    return num1 * num2

def divided(num1, num2):
    return num1 / num2


def calculator(num1, operation, num2):
    if operation == "+":
        return addition(num1, num2)
    elif operation == "-":
        return minus(num1, num2)
    elif operation == "*":
        return times(num1, num2)
    elif operation == "/":
        return divided(num1, num2)
    else:
        print("error")

num1 = int(input("input a number: "))
operation = input("input a operation(+,-,*./): ")
num2 = int(input("input a number: "))

result = calculator(num1, operation, num2)
print(result)