def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum > target:
            r = r - 1
        elif sum < target:
            l = l + 1
        else:
            return([l+1, r+1])
