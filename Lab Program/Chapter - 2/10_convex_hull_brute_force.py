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
    if n <= 2:
        return points.copy()

    hull_edges = []

    for i in range(n):
        for j in range(i + 1, n):
            signs = []

            for k in range(n):
                if k == i or k == j:
                    continue
                signs.append(orientation(points[i], points[j], points[k]))

            # An edge belongs to the convex hull if all other points
            # lie on one side or on the line.
            if all(s >= 0 for s in signs) or all(s <= 0 for s in signs):
                hull_edges.append((points[i], points[j]))

    hull_points = set()
    for a, b in hull_edges:
        hull_points.add(a)
        hull_points.add(b)

    # Order hull points counter-clockwise around their centroid.
    center_x = sum(p[0] for p in hull_points) / len(hull_points)
    center_y = sum(p[1] for p in hull_points) / len(hull_points)

    import math
    ordered = sorted(
        hull_points,
        key=lambda p: math.atan2(p[1] - center_y, p[0] - center_x)
    )

    return ordered

points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
print("Convex Hull:", convex_hull_brute_force(points))
