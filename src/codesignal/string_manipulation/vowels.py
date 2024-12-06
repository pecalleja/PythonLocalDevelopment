"""
Write a function that takes a string s, iterates through it, and collects all
0-based positions of vowels in it to a list.
Note that you should not use any Python built-in string methods to solve this
task.
For example, print(solution("Hello WORLD")) should output [1, 4, 7].
Here, 'e' is a vowel, and its position in the string "Hello" is 1. 'o' is also
a vowel, and its position is 4. The last vowel is O at position 7.
"""


def solution(s):
    # TODO: implement find_vowels_positions
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = []
    for i, char in enumerate(s):
        if char in vowels:
            result.append(i)
    return result
