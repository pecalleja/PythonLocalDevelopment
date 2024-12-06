"""
Given a string, you need to return a new string where every letter is shifted
 to its right by one place in alphabetical order. The last letters z and Z
 should be replaced with the first ones: a and A, respectively. If the
 character isn't a letter, it should stay the same.

It is not allowed to use string built-in methods here.

For example, given the string "abc123XYz!",
the function should return "bcd123YZa!".
"""


def solution(s):
    result = []

    for c in s:
        number = ord(c)
        if ord("a") <= number <= ord("z") or ord("A") <= number <= ord("Z"):
            if number == ord("z"):
                number = ord("a")
            elif number == ord("Z"):
                number = ord("A")
            else:
                number += 1
            result.append(chr(number))
        else:
            result.append(c)
    return "".join(result)
