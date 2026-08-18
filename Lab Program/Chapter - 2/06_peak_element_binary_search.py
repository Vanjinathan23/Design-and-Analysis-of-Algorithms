def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

test_cases = [
    [1, 2, 3, 1],
    [1, 2, 1, 3, 5, 6, 4]
]

for nums in test_cases:
    index = find_peak_element(nums)
    print("Array:", nums)
    print("Peak index:", index)
    print("Peak value:", nums[index])
    print()
