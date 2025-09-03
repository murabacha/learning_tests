while True:   
    rows = int(input('enter the number of rows you want '))

    for i in range(1 ,rows+1):
        for space in range(1, rows-i +1 ):
            print(end=' ')
        for stars in range(1,i):
            print('*' ,end=' ')
        print('')
