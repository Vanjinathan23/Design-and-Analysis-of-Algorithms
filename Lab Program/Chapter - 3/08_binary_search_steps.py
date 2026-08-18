def binary_search_steps(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        print(f"low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


test_cases = [
    ([3, 9, 14, 19, 25, 31, 42, 47, 53], 31),
    ([13, 19, 24, 29, 35, 41, 42], 42),
    ([20, 40, 60, 80, 100, 120], 60)
]

for arr, key in test_cases:
    print("Array:", arr)
    print("Search key:", key)
    index, comparisons = binary_search_steps(arr, key)
    print("Index (0-based):", index)
    print("Position (1-based):", index + 1 if index != -1 else -1)
    print("Comparisons:", comparisons)
    print()

print("If the array is not sorted:")
print("- Binary Search may discard the half containing the key.")
print("- The result can therefore be incorrect.")
print("- The O(log n) correctness guarantee requires sorted data.")
print("- For an unsorted array, use linear search or sort first.")
