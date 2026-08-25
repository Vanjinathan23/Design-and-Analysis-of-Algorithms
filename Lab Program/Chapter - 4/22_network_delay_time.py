import heapq

def network_delay_time(times, n, k):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in times:
        graph[u].append((v, w))

    dist = [float("inf")] * (n + 1)
    dist[k] = 0

    heap = [(0, k)]

    while heap:
        time, node = heapq.heappop(heap)

        if time > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_time = time + weight

            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))

    answer = max(dist[1:])

    return -1 if answer == float("inf") else answer

print("Example 1:", network_delay_time(
    [[2,1,1],[2,3,1],[3,4,1]], 4, 2
))

print("Example 2:", network_delay_time(
    [[1,2,1]], 2, 1
))

print("Example 3:", network_delay_time(
    [[1,2,1]], 2, 2
))
