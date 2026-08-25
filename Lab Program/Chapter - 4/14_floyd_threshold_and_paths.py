INF=float("inf")
def solve(n,edges,threshold):
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for u,v,w in edges: d[u][v]=d[v][u]=w
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    counts=[sum(1 for j in range(n) if i!=j and d[i][j]<=threshold) for i in range(n)]
    city=min(range(n),key=lambda i:(counts[i],-i))
    return city,d

edges=[(0,1,2),(0,4,8),(1,2,3),(1,4,2),(2,3,1),(3,4,1)]
city,d=solve(5,edges,2)
print("City with smallest reachable neighbors:",city)
