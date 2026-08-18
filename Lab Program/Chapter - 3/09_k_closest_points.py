def k_closest_points(points, k):
    return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


test_cases = [
    ([[1, 3], [-2, 2], [5, 8], [0, 1]], 2),
    ([[1, 3], [-2, 2]], 1),
    ([[3, 3], [5, -1], [-2, 4]], 2)
]

for points, k in test_cases:
    print("Points:", points)
    print("k =", k)
    print("Output:", k_closest_points(points, k))
    print()
