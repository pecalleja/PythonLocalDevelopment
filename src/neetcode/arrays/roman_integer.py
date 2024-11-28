class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        i = 0
        total = len(s)
        ans = 0
        while i < total:
            letter = s[i]
            next_letter = s[i + 1] if i < total - 1 else ""
            if f"{letter}{next_letter}" in table:
                letter = f"{letter}{next_letter}"
                i += 2
            else:
                i += 1
            ans += table[letter]
        return ans
