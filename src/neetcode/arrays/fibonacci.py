class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        def recursive_fib(e):
            if e in cache:
                return cache[e]

            if e < 2:
                return e
            else:
                ans = recursive_fib(e - 1) + recursive_fib(e - 2)

            cache[e] = ans
            return ans

        return recursive_fib(n)
