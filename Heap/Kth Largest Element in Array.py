def findKthLargest(self, nums: List[int], k: int) -> int:
    # sort: O(NlogN)
    # nums.sort(reverse = True)
    # return(nums[k-1])

    # heap O(nlogk)
    for i in range(len(nums)):
        nums[i] *= -1

    heapq.heapify(nums)

    i = 0
    while i < k:
        ans = heapq.heappop(nums)
        i += 1
    return -ans