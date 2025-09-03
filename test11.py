x = int(input('enter the start number\n'))
y = int(input('enter the end number\n'))

print(f'prime numbers between {x} and {y} are :\n')
for num in range(x , y+1):
    if num > 1:
        is_prime = True
        for i in range(num-1 , 1 , -1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)    
