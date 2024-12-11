class Solution:
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

    def romanToInt(self, s: str) -> int:

        i = 0
        total = len(s)
        ans = 0
        while i < total:
            letter = s[i]
            next_letter = s[i + 1] if i < total - 1 else ""
            if f"{letter}{next_letter}" in self.table:
                letter = f"{letter}{next_letter}"
                i += 2
            else:
                i += 1
            ans += self.table[letter]
        return ans

    def intToRoman(self, num: int) -> str:
        # Sort the dictionary items by values in descending order
        sorted_table = sorted(self.table.items(), key=lambda x: -x[1])

        result = []
        for symbol, value in sorted_table:
            while num >= value:
                num -= value
                result.append(symbol)

        return "".join(result)
