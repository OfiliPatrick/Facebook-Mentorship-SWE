
# with memoization

def fib1(n):
    memo_cache = {}
    def helper(n):
        if n in memo_cache:
            return memo_cache[n]

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1 

        result = helper(n - 1) + helper(n - 2)
        memo_cache[n] = result
        return result

    return helper(n)


#without memoization

def fib2(n):
    if n == 1 or n == 2:
        return 1 
    return fib2(n-1) + fib2(n-2)

for i in range(1,100):
    print(fib1(i))



