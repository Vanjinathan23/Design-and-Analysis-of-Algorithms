from bisect import bisect_left


def subset_sums(values):
    result = []

    for mask in range(1 << len(values)):
        total = 0
        subset = []

        for i, value in enumerate(values):
            if mask & (1 << i):
                total += value
                subset.append(value)

        result.append((total, subset))

    return result


def closest_subset_sum(values, target):
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)
    right_sums.sort(key=lambda x: x[0])

    right_values = [x[0] for x in right_sums]

    best_sum = None
    best_subset = []
    best_difference = float("inf")

    for left_sum, left_subset in left_sums:
        needed = target - left_sum
        pos = bisect_left(right_values, needed)

        for index in (pos - 1, pos):
            if 0 <= index < len(right_sums):
                right_sum, right_subset = right_sums[index]
                total = left_sum + right_sum
                difference = abs(target - total)

                if difference < best_difference:
                    best_difference = difference
                    best_sum = total
                    best_subset = left_subset + right_subset

    return best_subset, best_sum, best_difference


test_cases = [
    ([45, 34, 4, 12, 5, 2], 42),
    ([1, 3, 2, 7, 4, 6], 10)
]

for values, target in test_cases:
    subset, total, difference = closest_subset_sum(values, target)
    print("Set:", values)
    print("Target:", target)
    print("Closest subset:", subset)
    print("Subset sum:", total)
    print("Difference:", difference)
    print()
