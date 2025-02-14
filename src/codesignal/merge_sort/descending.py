def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_desc(left)
    right = merge_sort_desc(right)

    return merge_desc(left, right)


def merge_desc(left, right):
    res = []
    left_index, right_index = (0, 0)

    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1
    if left:
        res.extend(left[left_index:])
    if right:
        res.extend(right[right_index:])

    return res
