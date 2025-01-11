class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        def recursive_fib(e):
            if e not in cache:
                cache[e] = recursive_fib(e - 1) + recursive_fib(e - 2)
            return cache[e]

        return recursive_fib(n)
