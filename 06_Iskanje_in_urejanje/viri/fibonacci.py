def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib2(n):
    if n <= 1:
        return 1
    an = 1
    an1 = 1
    for i in range(2, n + 1):
        an, an1 = an + an1, an
    return an
