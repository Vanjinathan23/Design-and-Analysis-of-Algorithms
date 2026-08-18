def quick_sort(arr, low=0, high=None, steps=None):
    if high is None:
        high = len(arr) - 1
        steps = []

    if low < high:
        pivot_index = partition(arr, low, high)
        steps.append(("After partition", arr.copy(), pivot_index))

        quick_sort(arr, low, pivot_index - 1, steps)
        steps.append(("After left recursive call", arr.copy(), None))

        quick_sort(arr, pivot_index + 1, high, steps)
        steps.append(("After right recursive call", arr.copy(), None))

    return arr, steps


def partition(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]

    # Move pivot to the end temporarily.
    arr[mid], arr[high] = arr[high], arr[mid]

    store = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1

    arr[store], arr[high] = arr[high], arr[store]
    return store


test_cases = [
    [19, 72, 35, 46, 58, 91, 22, 31],
    [31, 23, 35, 27, 11, 21, 15, 28],
    [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
]

for arr in test_cases:
    sorted_arr, steps = quick_sort(arr.copy())
    print("Input :", arr)
    for label, state, pivot_index in steps:
        print(label + ":", state, end="")
        if pivot_index is not None:
            print(" | Pivot index:", pivot_index)
        else:
            print()
    print("Output:", sorted_arr)
    print()
