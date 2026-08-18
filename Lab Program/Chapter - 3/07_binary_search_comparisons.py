def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == key:
            # 1-based position is printed below to match the supplied examples.
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


test_cases = [
    ([5, 10, 15, 20, 25, 30, 35, 40, 45], 20),
    ([10, 20, 30, 40, 50, 60], 50),
    ([21, 32, 40, 54, 65, 76, 87], 32)
]

for arr, key in test_cases:
    index, comparisons = binary_search(arr, key)
    print("Array:", arr)
    print("Search key:", key)
    print("Index (0-based):", index)
    print("Position (1-based):", index + 1 if index != -1 else -1)
    print("Comparisons:", comparisons)
    print()
