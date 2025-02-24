import random


def find_kth_smallest(numbers, k):
    if numbers:
        pos = partition(numbers, 0, len(numbers) - 1)
        if k - 1 == pos:
            # The pivot is the k-th element after partitioning
            return numbers[pos]
        elif k - 1 < pos:
            # The pivot index after partitioning is larger than k
            # We'll keep searching in the left part
            return find_kth_smallest(numbers[:pos], k)
        else:
            # The pivot index after partitioning is smaller than k
            # We'll keep searching in the right part
            return find_kth_smallest(numbers[pos + 1 :], k - pos - 1)  # noqa


def partition(nums, left, right):
    # Choosing a random index to make the algorithm less deterministic
    rand_index = random.randint(left, right)
    nums[left], nums[rand_index] = nums[rand_index], nums[left]
    pivot_index = left
    for i in range(left + 1, right + 1):
        if nums[i] <= nums[left]:
            pivot_index += 1
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
    nums[pivot_index], nums[left] = nums[left], nums[pivot_index]
    return pivot_index
