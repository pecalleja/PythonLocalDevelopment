class Solution:
    def climbStairs(self, x: int) -> int:
        cache = {}

        def recursive_steps(n):
            if n in cache:
                return cache[n]
            if n < 4:
                return n
            ans = recursive_steps(n - 1) + recursive_steps(n - 2)
            cache[n] = ans
            return ans

        return recursive_steps(x)
