"""
Generating All Unique Combinations Using Backtracking

You are provided with an array of n integers, which may contain duplicate
elements. Write a recursive function that generates all distinct permutations
of the numbers in the array. The permutations need to be of the same length as
the input array, and they should be in lexicographically sorted order.

Use a method similar to backtracking to solve this task. The function should
return an array of all these permutations. The expected time complexity for
the solution is O(N!).

Note: You cannot use a built-in Python function or library method to directly
generate permutations. The intention here is to specifically practice
recursion and backtracking techniques.
"""


def solution(nums):
    def backtrack(counter, curr_perm, result):
        # If current permutation is complete
        if len(curr_perm) == len(nums):
            result.append(curr_perm[:])
            return

        # Try each unique number from counter
        for num in sorted(counter.keys()):
            if counter[num] > 0:
                # Use the number
                counter[num] -= 1
                curr_perm.append(num)

                # Recurse
                backtrack(counter, curr_perm, result)

                # Backtrack
                curr_perm.pop()
                counter[num] += 1

    # Create counter dictionary
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    result = []
    backtrack(counter, [], result)
    return result
