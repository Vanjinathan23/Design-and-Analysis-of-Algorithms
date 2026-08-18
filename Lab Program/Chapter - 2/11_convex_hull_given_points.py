def orientation(a, b, c):
    value = ((b[0] - a[0]) * (c[1] - a[1]) -
             (b[1] - a[1]) * (c[0] - a[0]))
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

def convex_hull_brute_force(points):
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            signs = [
                orientation(points[i], points[j], points[k])
                for k in range(n) if k != i and k != j
            ]

            if all(s >= 0 for s in signs) or all(s <= 0 for s in signs):
                edges.append((points[i], points[j]))

    hull = set()
    for a, b in edges:
        hull.add(a)
        hull.add(b)

    cx = sum(p[0] for p in hull) / len(hull)
    cy = sum(p[1] for p in hull) / len(hull)

    import math
    return sorted(hull, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

points = [
    (10, 0), (11, 5), (5, 3), (9, 3.5),
    (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)
]

print("Convex Hull:", convex_hull_brute_force(points))
