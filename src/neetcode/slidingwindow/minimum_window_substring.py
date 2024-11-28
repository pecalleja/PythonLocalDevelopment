class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        required = len(t_count)
        formed = 0
        window_counts = {}

        l, r = 0, 0
        min_len = float("inf")
        min_window = ""

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = s[l : r + 1]  # noqa

                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                l += 1

            r += 1

        return min_window
