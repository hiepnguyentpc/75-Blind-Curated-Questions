def minSubArrLen(nums, target):
    l = 0

    res = float('inf')

    sum = 0
    for r in range(len(nums)):
        sum += nums[r]

        while sum >= target:
            res = min(res, r - l + 1)
            sum -= nums[l]
            l += 1
    return res if res != float('inf') else 0



nums1 = [2,3,1,2,4,3]
target1 = 7
print(minSubArrLen(nums1, target1))