def count_inversions(arr):
    # The code is very similar to the merge_sort implementation
    # The main difference lies in the merge_count_inversions function
    if len(arr) <= 1:
        return arr, 0
    else:
        middle = int(len(arr) / 2)
        left, a = count_inversions(arr[:middle])
        right, b = count_inversions(arr[middle:])
        result, c = merge_count_inversions(left, right)
        return result, (a + b + c)


def merge_count_inversions(x, y):
    count = 0
    i, j = 0, 0
    merged = []
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            merged.append(x[i])
            i += 1
        else:
            merged.append(y[j])
            j += 1
            # Here, we update the number of inversions
            # Every element from x[i:] and y[j] forms an inversion
            count += len(x) - i
    merged += x[i:]
    merged += y[j:]
    return merged, count
