#fibonaccci sequence 
a = int (input('enter the number you want to get the fibonacci sequebce of\n '))
def f(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return f(n-1)+f(n-2)
print(f(a))
