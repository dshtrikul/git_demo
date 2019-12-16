import time

num = 100


def timer(runs):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(runs, f'runs with params {args, kwargs}')
            start = time.time()
            for i in range(runs):
                func(*args, **kwargs)
                delta = time.time() - start
                print(f'time: {delta:.5f}')
            return func(*args, **kwargs)
        return wrapper
    return inner


@timer(runs=1)
def fib(num):
    return list(fib_gen(num))


def fib_gen(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n-2) + fib_recursive(n-1)


@timer(runs=1)
def fib_r(n):
    return list(fib_recursive(i) for i in range(n))


fib(50)
for i in range(30, 40):
    fib_r(i)




