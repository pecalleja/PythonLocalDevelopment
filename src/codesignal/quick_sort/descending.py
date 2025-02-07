"""
Implementing Quick Sort for Descending Order from Scratch

Create Quick Sort function that can sort a list of 20 random numbers in
descending order from scratch!
"""


def partition_desc(arr, low, high):
    """
    Partition the array for descending order Quick Sort.
    The pivot is chosen as the last element.
    All elements greater than or equal to the pivot are moved to the left,
    and elements smaller than the pivot to the right.
    """
    pivot = arr[high]
    i = low - 1  # index of the greater element

    for j in range(low, high):
        # For descending order, we want larger elements to come first.
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_desc(arr, low, high):
    """
    The main Quick Sort function that recursively sorts the array in descending order.
    """  # noqa
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition_desc(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort_desc(arr, low, pivot_index - 1)
        quick_sort_desc(arr, pivot_index + 1, high)
