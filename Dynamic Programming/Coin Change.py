def coinChange(coins, amount):

    min_nums_coins = [float('inf')]*(amount + 1)
    min_nums_coins[0] = 0

    for coin in coins:
        for target in range(coin, amount + 1):
            min_nums_coins[target] = min(min_nums_coins[target], min_nums_coins[target - coin] + 1)
    return min_nums_coins[amount] if min_nums_coins[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))