def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]

    for value in arr[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return minimum, maximum


test_cases = [
    [5, 7, 3, 4, 9, 12, 6, 2],
    [1, 3, 5, 7, 9, 11, 13, 15, 17],
    [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
]

for arr in test_cases:
    minimum, maximum = find_min_max(arr)
    print("Input :", arr)
    print("Min =", minimum, "Max =", maximum)
    print()
