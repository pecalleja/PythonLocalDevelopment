"""
Given a string input_string, your task is to write a function that transforms
all the lowercase letters to uppercase and all the uppercase letters to
lowercase. If the character is not a letter, do not transform it.

The transformation should be done without using any built-in Python methods,
it is not allowed to use built-in Python functions like lower(), upper(),
or similar in your code.

For example, for the input string "HelLo WoRld 123", the output should
be "hELlO wOrLD 123".
"""


def solution(input_string):
    result = []
    for char in input_string:
        number = ord(char)
        if ord("a") <= number <= ord("z"):
            result.append(chr(number - 32))
        elif ord("A") <= number <= ord("Z"):
            result.append(chr(number + 32))
        else:
            result.append(char)

    return "".join(result)
