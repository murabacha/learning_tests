#simple calculator with functions
def add(num1, num2):
    return num1 + num2


def divide(num1,num2):
    return num1 / num2

def multiplication(num1,num2):
    return num1 * num2

def subtract(num1,num2):
    return num1 - num2
while True:
    a =int(input('enter the first number\n'))
    b = int(input('enter the second number\n'))
    operator = input('select operator\n 1:add\n2:divide\n3:multiplication' \
    '\n4:subtract')
    if operator == '1':
        print(add(a,b))
    elif operator == '2':
        print(divide(a,b))
    elif operator == '3':
        print(multiplication(a,b))
    else:
        print(subtract(a,b))
