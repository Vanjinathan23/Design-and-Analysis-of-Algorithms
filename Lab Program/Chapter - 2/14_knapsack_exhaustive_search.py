import itertools

def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

def knapsack_exhaustive(weights, values, capacity):
    n = len(weights)

    best_items = []
    best_value = 0

    for mask in range(1 << n):
        selected = [
            i for i in range(n)
            if mask & (1 << i)
        ]

        if is_feasible(selected, weights, capacity):
            value = total_value(selected, values)

            if value > best_value:
                best_value = value
                best_items = selected

    return best_items, best_value

test_cases = [
    ([2, 3, 1], [4, 5, 3], 4),
    ([1, 2, 3, 4], [2, 4, 6, 3], 6)
]

for i, (weights, values, capacity) in enumerate(test_cases, 1):
    selected, value = knapsack_exhaustive(weights, values, capacity)
    print(f"Test Case {i}:")
    print("Optimal Selection:", selected)
    print("Total Value:", value)
    print()
