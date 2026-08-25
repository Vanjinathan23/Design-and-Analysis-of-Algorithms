def dice_throw(num_sides, num_dice, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    for d in range(1, num_dice + 1):
        for s in range(1, target + 1):
            dp[d][s] = sum(dp[d-1][s-face] for face in range(1, num_sides + 1) if s-face >= 0)
    return dp[num_dice][target]

print("Test Case 1:", dice_throw(6, 2, 7))
print("Test Case 2:", dice_throw(4, 3, 10))
