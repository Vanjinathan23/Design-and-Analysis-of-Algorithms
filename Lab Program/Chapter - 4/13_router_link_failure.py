INF=float("inf")
routers=["A","B","C","D","E","F"]
edges=[(0,1,1),(0,2,5),(1,2,2),(1,3,1),(2,4,3),(3,4,1),(3,5,6),(4,5,2)]

def shortest(edges):
    d=[[INF]*6 for _ in range(6)]
    for i in range(6): d[i][i]=0
    for u,v,w in edges: d[u][v]=d[v][u]=w
    for k in range(6):
        for i in range(6):
            for j in range(6): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

before=shortest(edges)
after=shortest([e for e in edges if set(e[:2])!={1,3}])
print("A to F before failure:",before[0][5])
print("A to F after failure:",after[0][5])
