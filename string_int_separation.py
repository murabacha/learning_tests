x = [1,2,'AS',4,'W',6]
y = []
z = []
for i in range(len(x)):
    if type(x[i]) == str:
        y.append(x[i])
    else:
        z.append(x[i])
print(y)
print(z)
