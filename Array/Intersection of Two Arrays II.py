def intersect(nums1, nums2):
    hashmap = dict()
    result = []
    for item in nums1:
        if item not in hashmap:
            hashmap[item] = 1
        else:
            hashmap[item] += 1
    for item in nums2:
        if item in hashmap and hashmap[item] > 0:
            result.append(item)
            hashmap[item] -= 1
    return result