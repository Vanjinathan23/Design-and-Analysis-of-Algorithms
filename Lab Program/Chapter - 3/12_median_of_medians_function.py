def median_of_medians(arr, k):
    """Return the 1-based k-th smallest element."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and len(arr)")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]

    pivot = median_of_medians(medians, (len(medians) + 1) // 2)

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k <= len(less):
        return median_of_medians(less, k)

    if k <= len(less) + len(equal):
        return pivot

    return median_of_medians(
        greater,
        k - len(less) - len(equal)
    )


test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
    ([23, 17, 31, 44, 55, 21, 20, 18, 19, 27], 5)
]

for arr, k in test_cases:
    print("Array:", arr)
    print("k =", k)
    print("k-th smallest:", median_of_medians(arr, k))
    print()
