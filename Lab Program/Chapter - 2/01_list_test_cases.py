def process_list(arr):
    return sorted(arr)

test_cases = [
    [],
    [1],
    [7, 7, 7, 7],
    [-5, -1, -3, -2, -4]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", process_list(arr))
    print()
