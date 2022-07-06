class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance = {}
        for i in range(len(nums)):
            if nums[i] not in occurance:
                occurance[nums[i]] = 1
            else:
                occurance[nums[i]] += 1

        occurance_sorted = dict(sorted(occurance.items(), key=lambda item: item[1]))

        numbers = list(occurance_sorted.keys())
        print(numbers)

        res = []
        for i in range(k):
            res.append(numbers[i])
        return res
