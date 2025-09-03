
while True:
    v = int(input('enter the number of rows: \n'))
    for i in range(1,v+1):
        for j in range(1,i+1):
            print("*", end=' ')
        print('')
    for x in range(v-1,0,-1):
        for y in range(x):
            print('*',end=' ')
        print('')
        

