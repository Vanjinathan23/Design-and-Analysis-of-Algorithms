def subset_sums(values):
    sums = set()

    for mask in range(1 << len(values)):
        total = 0

        for i, value in enumerate(values):
            if mask & (1 << i):
                total += value

        sums.add(total)

    return sums


def subset_sum_exists(values, target):
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    for left_sum in left_sums:
        if target - left_sum in right_sums:
            return True

    return False


test_cases = [
    ([1, 3, 9, 2, 7, 12], 15),
    ([3, 34, 4, 12, 5, 2], 15)
]

for values, target in test_cases:
    print("Set:", values)
    print("Exact Sum:", target)
    print("Result:", subset_sum_exists(values, target))
    print()
