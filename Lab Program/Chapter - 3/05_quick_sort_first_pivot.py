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
    # First element is the pivot.
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i > j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


test_cases = [
    [10, 16, 8, 12, 15, 6, 3, 9, 5],
    [12, 4, 78, 23, 45, 67, 89, 1],
    [38, 27, 43, 3, 9, 82, 10]
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
