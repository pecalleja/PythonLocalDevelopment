"""
Finding the Most Frequent Substring

Your task is to design an algorithm that, given a string text and an integer
length, returns the maximum number of times any substring of length occurs in
text.
For instance, consider the following scenario:
text = "abrakadabraka"
length = 3
print(max_substring_occurrences(text, length)) # output: 2

In the above example, the maximum number of times any substring of length 3
appears in the given text is 2 - for example, the substring "abr".
"""


def solution(text, length):
    if not text or length > len(text):
        return 0

    # Use a prime number for the base and modulo to minimize collisions
    base = 26  # Assuming lowercase letters only; adjust if needed
    mod = 10**9 + 7

    # Precompute the largest power needed
    power = pow(base, length - 1, mod)

    # Calculate initial hash value
    curr_hash = 0
    hash_count = {}  # Dictionary to store hash counts

    # Calculate initial window hash
    for i in range(length):
        curr_hash = (curr_hash * base + ord(text[i])) % mod
    hash_count[curr_hash] = 1

    # Slide the window and update hash
    for i in range(length, len(text)):
        # Remove leftmost character of previous window
        curr_hash = (curr_hash - ord(text[i - length]) * power) % mod
        # Add new character
        curr_hash = (curr_hash * base + ord(text[i])) % mod
        # Ensure hash is positive
        curr_hash = (curr_hash + mod) % mod
        # Update count
        hash_count[curr_hash] = hash_count.get(curr_hash, 0) + 1

    return max(hash_count.values())
