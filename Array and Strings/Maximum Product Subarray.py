"""
def maxProduct(nums):
    max = 0
    product = 1
    if len(nums) == 1:
        return nums[0]
    else:
        for i in range(len(nums)):
            if i == len(nums) - 1 and nums[i] > max:
                return nums[i]
            j = i + 1
            while (product > max and j < len(nums)):
                product = nums[i]*nums[j]
                max = product
                j = j + 1
        return max

nums = [0,2]
print(maxProduct(nums))
"""



def maxProduct(nums):
    min_so_far = nums[0]
    max_so_far = nums[0]

    result = max_so_far

    for i in range(1,len(nums)):
        temp_max = max(nums[i], nums[i]*max_so_far, nums[i]*min_so_far)
        min_so_far = max(nums[i], nums[i]*max_so_far, nums[i]*min_so_far)
        max_so_far = temp_max
        result = max(max_so_far, result)
    return result





