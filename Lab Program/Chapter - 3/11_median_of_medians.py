def median_of_medians(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and len(arr)")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]

    pivot = median_of_medians(medians, (len(medians) + 1) // 2)

    lows = [x for x in arr if x < pivot]
    equals = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    if k <= len(lows):
        return median_of_medians(lows, k)
    elif k <= len(lows) + len(equals):
        return pivot
    else:
        return median_of_medians(
            highs,
            k - len(lows) - len(equals)
        )


test_cases = [
    ([12, 3, 5, 7, 19], 2),
    ([12, 3, 5, 7, 4, 19, 26], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
]

for arr, k in test_cases:
    print("Array:", arr, "k =", k)
    print("Output:", median_of_medians(arr, k))
    print()
