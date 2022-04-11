"""
extra space solution
def rotate(nums, k):
    subarray = [0]*len(nums)
    j = 0
    for i in range(len(nums)-k, len(nums)):
        subarray[j] = nums[i]
        j = j + 1
    for i in range(len(nums) - k):
        subarray[j] = nums[i]
        j += 1

    for i in range(len(nums)):
        nums[i] = subarray[i]
    return nums
"""
def rotate(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums)  - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1




nums = [1,2,3,4,5,6,7]
print(rotate(nums, 3))
