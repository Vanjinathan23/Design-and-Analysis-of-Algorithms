INF=float("inf")

def floyd_warshall(n, edges):
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for u,v,w in edges: d[u][v]=min(d[u][v],w)
    before=[row[:] for row in d]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return before,d

edges=[(0,1,3),(0,2,8),(0,3,-4),(1,3,1),(1,2,4),(2,0,2),(3,2,-5),(3,1,6)]
before,after=floyd_warshall(4,edges)
print("Before:",before)
print("After:",after)
print("City 1 to City 3:",after[0][2])
