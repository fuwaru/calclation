import math


def my_log(x):
    if x <= 0:
        return None
    elif x == 1:
        return 0
    else:
        n = 1000000
        return sum([((x-1)/x)**i/(2*i+1) for i in range(n)])*2
    

def myLog2(x, b):
    if x < b:
        return 0  
    return 1 + myLog2(x/b, b)

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def mylog(b, a):
    x = ln(b)/ln(a)
    return x

print(round(mylog(10,math.e)))

print(myLog2(10,math.e))

print(my_log(10))

print(math.log(10))