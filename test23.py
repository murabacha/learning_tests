array = [3,1,6,2,8,4,7]

for i in range (len(array)):
    for j in range(i+1,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            j = 1

print(array)
x = sorted(array)
print(x)