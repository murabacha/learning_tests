a = [1,2,3,4,5,6,7,8,9]
b = []
for i in range(len(a)):
    x = i+1
    while x < len(a):
        b.append((a[i],a[x]))
        x+=1

    
print(b)
