import itertools
import math

def distance(city1, city2):
    return math.sqrt(
        (city1[0] - city2[0]) ** 2 +
        (city1[1] - city2[1]) ** 2
    )

def tsp(cities):
    start = cities[0]
    remaining = cities[1:]

    shortest_distance = float("inf")
    shortest_path = None

    for permutation in itertools.permutations(remaining):
        path = [start] + list(permutation) + [start]

        total = sum(
            distance(path[i], path[i + 1])
            for i in range(len(path) - 1)
        )

        if total < shortest_distance:
            shortest_distance = total
            shortest_path = path

    return shortest_distance, shortest_path

test_cases = [
    [(1, 2), (4, 5), (7, 1), (3, 6)],
    [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
]

for i, cities in enumerate(test_cases, 1):
    d, path = tsp(cities)
    print(f"Test Case {i}:")
    print("Shortest Distance:", d)
    print("Shortest Path:", path)
    print()
