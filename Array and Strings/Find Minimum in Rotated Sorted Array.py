def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def find_rotate_index(left, right):
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            elif nums[pivot - 1] > nums[pivot]:
                return pivot
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1

    def search(left, right):
        while left <= right:
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            else:
                if nums[pivot] > target:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return -1

    n = len(nums)

    if n == 1:
        return 0 if nums[0] == target else -1
    rotate_index = find_rotate_index(0, n - 1)
    if nums[rotate_index] == target:
        return rotate_index
    if rotate_index == 0:
        return search(0, n - 1)
    if target < nums[0]:
        return search(rotate_index, n - 1)
    return search(0, rotate_index)
