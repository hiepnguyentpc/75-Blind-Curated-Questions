def BinarySearch(l, r, target):
    while l<=r:
        mid = l + (r-l)//2
        if mid > target:
            r = mid - 1
        elif mid < target:
            l = mid + 1
        else:
            return mid