import time
import functools
@functools.lru_cache()
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()

for i in range(1,100):
    result = fib(i)
    print("{}. {},delta time = {}".format(i, result, time.time()-start))

print(fib.cache_info())