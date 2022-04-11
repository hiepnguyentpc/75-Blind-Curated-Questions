
def twoSum(nums, target):
    hashmap = {}
    #archive value into hashmap
    #eg: hashmap[value of nums] = index of value in nums

    for i in range(len(nums)):
        hashmap[nums[i]] = i
    #if the complement of value is in the hashmap
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]



nums1 = [2,7,11,15]
target1 = 9
print(twoSum(nums1, target1))