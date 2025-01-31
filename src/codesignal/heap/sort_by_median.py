"""
Sorting Array by Absolute Difference with the Median

You have to sort an array of n integers but with a twist. The task requires
you to sort the integers according to their absolute difference from the
median of the array. If two numbers have the same absolute difference from the
median, the smaller number should be placed first.

Make sure to use a heap to ensure efficient sorting, you are not allowed to
use built-in methods like sort() or sorted().

The expected time complexity is O(nlogn).
"""

import heapq


def solution(arr):
    n = len(arr)
    if n == 0:
        return []

    # 1. Find the median via sorting (O(n log n))
    sorted_arr = sorted(arr)
    if n % 2 == 0:  # even
        median = sorted_arr[(n // 2) - 1]
    else:  # odd
        median = sorted_arr[n // 2]

    # 2. Push into a min-heap with the appropriate tie-break
    min_heap = []
    for x in arr:
        diff = abs(x - median)

        if n % 2 == 0:
            # even n => place ">= median" first when diff is tied
            side_flag = 0 if x >= median else 1
        else:
            # odd n => place smaller first when diff is tied
            side_flag = 0 if x < median else 1

        # The heap sorts primarily by (diff, side_flag, x)
        heapq.heappush(min_heap, (diff, side_flag, x))

    # 3. Pop from the heap
    result = []
    while min_heap:
        _, _, val = heapq.heappop(min_heap)
        result.append(val)

    return result
