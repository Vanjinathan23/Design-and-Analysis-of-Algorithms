from itertools import permutations

cities=["A","B","C","D","E"]
dist=[[0,10,15,20,25],[10,0,35,25,30],[15,35,0,30,20],[20,25,30,0,15],[25,30,20,15,0]]
best=float("inf"); route=None
for p in permutations(range(1,5)):
    r=(0,)+p+(0,)
    cost=sum(dist[r[i]][r[i+1]] for i in range(5))
    if cost<best: best,route=cost,r
print("Shortest route:", " -> ".join(cities[i] for i in route))
print("Total distance:", best)
