def func(x):
    return x * x
a= map(func,range(1,10))
print(list(a))

from functools import reduce
def f(x,y):
    return x + y
a = reduce(f,[1,3,5,7,9,10])
print(a)


def is_odd(x):
    return x % 2 == 1
a = filter(is_odd,[1,2,3,4,5,6,7,8])
print(list(a))




