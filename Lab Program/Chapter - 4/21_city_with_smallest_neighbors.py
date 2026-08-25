def find_the_city(n, edges, distanceThreshold):
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, weight in edges:
        dist[u][v] = weight
        dist[v][u] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    answer = -1
    minimum_count = float("inf")

    for city in range(n):
        reachable = sum(
            1 for other in range(n)
            if city != other and dist[city][other] <= distanceThreshold
        )

        if reachable <= minimum_count:
            minimum_count = reachable
            answer = city

    return answer

print("Example 1:", find_the_city(
    4,
    [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
    4
))

print("Example 2:", find_the_city(
    5,
    [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
    2
))
