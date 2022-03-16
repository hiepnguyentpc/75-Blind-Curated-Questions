def LengthOfLIS(nums):
    #Brute-force
    """
    count = [1]*(len(nums))
    for i in range(len(nums)):
        maximum = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > maximum:
                maximum = nums[j]
                count[i] += 1


    result = 0
    for i in range(len(nums)):
        result = max(result, count[i])
    return result
    """
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


nums = [10,9,2,5,3,7,101,18]
print(LengthOfLIS(nums))