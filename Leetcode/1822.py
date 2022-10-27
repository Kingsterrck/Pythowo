def arraySign(nums: [int]) -> int:
    if 0 in nums:
        return 0
    count = nums[0]
    for i in range(1, len(nums)):
        count *= nums[i]
    if count >0:
        return 1
    else:
        return -1


print(arraySign([-1, 1, -1, 1, -1]))
