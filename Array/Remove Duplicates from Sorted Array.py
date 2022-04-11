def removeDuplicates(nums) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]: #bypass all duplicated elements
            i += 1 #increment i for the right next element assignment
            nums[i] = nums[j]
    return i + 1 #because i stops right before the last element of distinct numbers