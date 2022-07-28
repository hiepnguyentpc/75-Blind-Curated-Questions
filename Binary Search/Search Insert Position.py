class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # nums = [1,3,5,6]

        # mid = (l+r)/2 == 2
        # if nums[mid] == target:
        # elif nums[mid] < target
        # elif nums[mid] > target

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l