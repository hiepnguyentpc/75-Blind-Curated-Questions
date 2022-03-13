def maxProfit(prices):
    minprice = 10000 + 1
    maxprice = 0

    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprice:
            maxprice = prices[i] - minprice

    return maxprice

prices = [7,1,5,3,6,4]
print(maxProfit(prices))