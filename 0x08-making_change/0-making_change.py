#!/usr/bin/python3

# function to find the minimum number of coins required to make
# up a given total amount, given a list of coin denominations

def makeChange(coins, total):
    if total <= 0:
        return 0
    # create a list to store the minimum number of coins required 
    # for each amount from 0 to the given total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are required to make up an amount of 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
