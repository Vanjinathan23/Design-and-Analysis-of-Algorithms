import heapq

def max_probability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]

    for (u, v), prob in zip(edges, succProb):
        graph[u].append((v, prob))
        graph[v].append((u, prob))

    best = [0.0] * n
    best[start] = 1.0
    heap = [(-1.0, start)]

    while heap:
        probability, node = heapq.heappop(heap)
        probability = -probability

        if node == end:
            return probability

        if probability < best[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = probability * edge_prob

            if new_prob > best[neighbor]:
                best[neighbor] = new_prob
                heapq.heappush(heap, (-new_prob, neighbor))

    return 0.0

edges = [[0,1],[1,2],[0,2]]

print("Example 1:", max_probability(
    3, edges, [0.5, 0.5, 0.2], 0, 2
))

print("Example 2:", max_probability(
    3, edges, [0.5, 0.5, 0.3], 0, 2
))
