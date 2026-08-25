def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    root = [[-1] * n for _ in range(n)]
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            total = prefix[j] - prefix[i]
            cost[i][j] = float("inf")

            for r in range(i, j):
                value = cost[i][r] + cost[r + 1][j] + total
                if value < cost[i][j]:
                    cost[i][j] = value
                    root[i][j - 1] = r

    return cost, root

keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]

cost, root = optimal_bst(keys, freq)

print("Optimal BST Cost:", cost[0][len(keys)])
print("\nCost Matrix:")
for row in cost:
    print(row)

print("\nRoot Matrix:")
for row in root:
    print(row)

print("\nTest Case 1:")
c1, _ = optimal_bst([10, 12], [34, 50])
print("Cost:", c1[0][2])

print("\nTest Case 2:")
c2, _ = optimal_bst([10, 12, 20], [34, 8, 50])
print("Cost:", c2[0][3])
