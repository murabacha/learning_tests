#fizz_buzz algorithm 

num = int(input('enter the number\n'))
def fizz_buzz(number):
    if num % 3 == 0 and num % 5 == 0:
        print('fizz_buzz')
    elif num % 3 == 0:
        print('fuzz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
fizz_buzz(num)