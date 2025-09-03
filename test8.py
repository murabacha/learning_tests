cars = ('audi','mercedes','howo')
while True:
    temp = list(cars)
    choices = input('select {1} to update or\n {2} to add\n or {3} to remove\n or {4} to delete entire tuple')
    if choices == '1':
        print(temp)
        y = int(input('which number do you want to change\n'))
        z = input('enter the value of the new item\n')
        temp[y-1] = z
        cars = tuple(temp)
        print(cars)
    elif choices == '3':
        print(temp)  
        n = input('enter the item you want to remove').strip().lower()  
        temp.remove(n)
        cars = tuple(temp)
        print(cars)
    elif choices == '4':
        del cars
        print('the tuple was deleted')
    
    else:
        x= input('how many items do you want to add\n ')
        for i in range(int(x)):
            temp.append(input('enter the item you want to add\n'))
            cars = tuple(temp)
        print(cars)