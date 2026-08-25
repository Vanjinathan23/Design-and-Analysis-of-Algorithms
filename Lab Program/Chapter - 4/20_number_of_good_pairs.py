def num_identical_pairs(nums):
    count = {}
    pairs = 0

    for num in nums:
        pairs += count.get(num, 0)
        count[num] = count.get(num, 0) + 1

    return pairs

print("Example 1:", num_identical_pairs([1, 2, 3, 1, 1, 3]))
print("Example 2:", num_identical_pairs([1, 1, 1, 1]))
