def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


test_cases = [
    [31, 23, 35, 27, 11, 21, 15, 28],
    [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
]

for arr in test_cases:
    print("Input :", arr)
    print("Output:", merge_sort(arr))
    print()
