"""
Brute-force solution
def maxProfit(prices) -> int:
    return calculatePrice(prices, 0)


def calculatePrice(prices, s) -> int:
    if s >= len(prices):
        return 0
    max = 0
    for i in range(s, len(prices)):
        max_profit = 0
        for j in range(s + 1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i] + calculatePrice(prices, j + 1)
                if profit > max_profit:
                    max_profit = profit
        if max_profit > max:
            max = max_profit
    return max

"""

#peak_valley solution

def maxProfit(prices) -> int:
    peak = prices[0]
    valley = prices[0]
    max = 0
    i = 0
    while (i < len(prices) - 1):
        while (i < len(prices) - 1 and prices[i+1] <= prices[i] ):
            i += 1
        valley = prices[i]

        while(i < len(prices) - 1 and prices[i+1] >= prices[i] ):
            i += 1
        peak = prices[i]

        max += (peak - valley)

    return max


prices = [7,1,5,3,6,4]
print(maxProfit(prices))




