#pi = input('enter your desired pi\n')
#radius = input('enter your desired radius\n')
#area = float(pi) * (float(radius) ** 2)
#print ('area of the circle is {0:.4f}' .format(area))
list = []
n = int(input('enter the number of values you want to enter\n '))
for i in range(n):
    values = input('enter your value\n ')
    list.append(values)

number_of_index = len(list)
number = number_of_index

index = input(f'enter index and this is the range is {{1}} to {{{number}}}\n')

word = list[int(index)-1]
print(f'the word is {word}')
print(list)

