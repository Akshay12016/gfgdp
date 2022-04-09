def fib(n,dict={}):
    if n in dict: return dict[n]
    if n<=2: return 1
    dict[n]=fib(n-1,dict)+fib(n-2,dict)
    return dict[n]
    

n=int(input('Enter the nth fibanoci number to be found:'))
print(fib(n))
