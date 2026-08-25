def min_production_time(times, transfer):
    n, m = len(times), len(times[0])
    dp = [[float("inf")]*n for _ in range(m)]
    for line in range(n): dp[0][line] = times[line][0]
    for s in range(1, m):
        for line in range(n):
            dp[s][line] = times[line][s] + min(dp[s-1][p] + transfer[p][line] for p in range(n))
    return min(dp[-1])

times=[[5,9,3],[6,8,4],[7,6,5]]
transfer=[[0,2,3],[2,0,4],[3,4,0]]
print("Minimum production time:", min_production_time(times, transfer))
