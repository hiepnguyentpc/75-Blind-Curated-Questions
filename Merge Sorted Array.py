

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0

    nums1Copy = nums1
    print(nums1Copy)
    for index in range(0, m+n):
        #if nums1 is over and there are still element in nums2
        #or nums1 is not over and element i <= element j
        if j >= n or (i < m and nums1Copy[i] <= nums2[j]):
            nums1[index] = nums1Copy[i]
            i = i + 1
        else:
            nums1[index] = nums2[j]
            j = j + 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 2

merge(nums1, m, nums2, n)
print(nums1)