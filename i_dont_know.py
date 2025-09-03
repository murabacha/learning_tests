fruits = []
fruit = input('enter the fruits\n ')
fruits1 = fruit.split()
#print(fruits1)
fruits.extend(fruits1)
print(fruits)
fruit_index = 0
fruit_number = int(len(fruits))
print(fruit_number)
word = input('enter fruit you want to sewarch\n')
fruit_found = False
while fruit_index < fruit_number:

    
    if fruits1[fruit_index] == (word):
        print(f'{word} is there')
        fruit_found = True
        break
    fruit_index+=1
    #else:
     #   print('no mangoes ')
    #break      
if not fruit_found:
    print(f'{word} not foung')
