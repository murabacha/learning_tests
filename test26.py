x = int(input('enter the start of the range\n'))
y = int(input('enter the end of the range \n'))
z = []
for i in range(x,y+1):
    if i > 1:
        is_prime = True
        for j in range(i-1,1,-1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime :
            z.append (i)
print (z)    
            

