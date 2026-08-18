def merge_sort(arr):
    comparisons = [0]

    def sort(values):
        if len(values) <= 1:
            return values

        mid = len(values) // 2
        left = sort(values[:mid])
        right = sort(values[mid:])

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons[0] += 1

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return sort(arr), comparisons[0]


test_cases = [
    [12, 4, 78, 23, 45, 67, 89, 1],
    [38, 27, 43, 3, 9, 82, 10]
]

for arr in test_cases:
    sorted_arr, comparisons = merge_sort(arr)
    print("Input :", arr)
    print("Sorted:", sorted_arr)
    print("Comparisons:", comparisons)
    print()
