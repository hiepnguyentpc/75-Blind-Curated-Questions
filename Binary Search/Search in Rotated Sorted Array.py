def BinarySearch(arr, l, r, target):
    while l<=r:
        middle = l + (r-l)//2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            r = middle - 1
        else:
            l = middle + 1
    return -1

def SearchinRotatedSorted(nums, target):
    pivot = 0
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            pivot = i
            return pivot





nums = [4,5,6,7,0,1,2]
target = 0
pivot = SearchinRotatedSorted(nums, target)
print(BinarySearch(nums, pivot+1, len(nums)-1, target))
