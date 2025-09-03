#selection sort algorithm
from random import random

a = []
for i in range (10000):
    a.append(i)

b = a.random()
c = sorted(b)
print(c)
n = len(b)
for i in range(0,n):
    for j in range(i+1,n):
        if b[j]<b[i]:
            b[i],b[j] = b[j],b[i]
        
print(b)