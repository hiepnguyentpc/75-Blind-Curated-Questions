def singleNumber(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    hashmap = {}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = 1
        else:
            hashmap[nums[i]] += 1

    for item in hashmap:
        if hashmap[item] == 1:
            return item

nums = [4,1,2,1,2]
print(singleNumber(nums))