def find_kth_positive(arr, k):
    missing = 0
    current = 1
    i = 0

    while True:
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            missing += 1
            if missing == k:
                return current
        current += 1

print(find_kth_positive([2, 3, 4, 7, 11], 5))  # 9
print(find_kth_positive([1, 2, 3, 4], 2))       # 6
