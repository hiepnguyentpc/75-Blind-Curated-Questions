def containsDuplicate(nums) -> bool:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        if nums[i] in hashmap and hashmap[nums[i]] != i:
            return True
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))