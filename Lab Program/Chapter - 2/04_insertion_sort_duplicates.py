def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Use > rather than >= so equal elements keep their relative order.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

test_cases = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 5, 5, 5, 5],
    [2, 3, 1, 3, 2, 1, 1, 3]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", insertion_sort(arr.copy()))
    print()
