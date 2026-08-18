import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    if len(points) < 2:
        return None, float("inf")

    min_distance = float("inf")
    closest = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
                closest = (points[i], points[j])

    return closest, min_distance

points = [(1, 2), (4, 5), (7, 8), (3, 1)]
pair, d = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", d)
