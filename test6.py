
dict_name = input('enter the name of the dictionary\n')
dict_name = {}
num = int(input('enter the number of items you want to enter\n'))

#key = input('enter the value of the key\n')

#value = input('enter the value\n')

for i in range(num):
    key = input('enter the value of the key\n')

    value = input('enter the value\n')
    dict_name.update ({int(key):value})
    print(dict_name)

