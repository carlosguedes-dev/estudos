from functools import lru_cache, partial, reduce

# LRU CACHE
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# PARTIAL
def multiplicar(a, b):
    return a * b

dobro = partial(multiplicar, 2)
# dobro(4) -> 8

# REDUCE
soma = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 15
