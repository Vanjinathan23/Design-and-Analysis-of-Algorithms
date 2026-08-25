from itertools import permutations

def tsp(dist):
    n=len(dist); best=float("inf")
    for p in permutations(range(1,n)):
        cost=dist[0][p[0]] + sum(dist[p[i]][p[i+1]] for i in range(n-2)) + dist[p[-1]][0]
        best=min(best,cost)
    return best

tests=[
[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]],
[[0,10,10,10],[10,0,10,10],[10,10,0,10],[10,10,10,0]],
[[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
]
for i,t in enumerate(tests,1): print(f"Test {i}:", tsp(t))
