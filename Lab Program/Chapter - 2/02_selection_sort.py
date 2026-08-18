def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

test_cases = [
    [5, 2, 9, 1, 5, 6],
    [10, 8, 6, 4, 2],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", selection_sort(arr.copy()))
    print()
