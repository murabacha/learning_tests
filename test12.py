x =int(input('enter the first number\n'))
y = int(input('enter the last number\n'))
print('even numbers:')
for i in range (x, y+1):
    if i % 2 == 0:
        print(i, end=',')
print()
print('odd numbers:')    
for x in range (x, y+1):
    if x % 2 != 0:
        print(x, end=',')