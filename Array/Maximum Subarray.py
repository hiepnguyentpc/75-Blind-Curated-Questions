#SLIDING WINDOW PATTERN

def maxSubArray(nums):
    max_local, max_global = nums[0], nums[0]
    for i in range(1, len(nums)):
        max_local = max(max_local, nums[i] + max_local)
        if max_local > max_global:
            max_global = max_local
    return max_global
