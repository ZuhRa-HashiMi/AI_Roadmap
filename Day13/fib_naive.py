def fib_naive(n):
    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)

print(fib_naive(10))


def cal_fib(n):
    f0 = 0
    f1 = 1
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    fn = None
    
    for i in range(1, n):
    
        fn = f0 + f1
        f0 = f1
        f1 = fn
        
        
    return fn

print(cal_fib(10))