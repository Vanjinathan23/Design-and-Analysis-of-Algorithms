def find_min_max_sorted(arr):
    # For an ascending sorted array, first = minimum and last = maximum.
    return arr[0], arr[-1]


test_cases = [
    [2, 4, 6, 8, 10, 12, 14, 18],
    [11, 13, 15, 17, 19, 21, 23, 35, 37],
    [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
]

for arr in test_cases:
    # The third test case is not sorted, so use the general method.
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        minimum, maximum = find_min_max_sorted(arr)
    else:
        minimum, maximum = min(arr), max(arr)

    print("Input :", arr)
    print("Min =", minimum, "Max =", maximum)
    print()
