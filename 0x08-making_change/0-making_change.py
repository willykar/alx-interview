#!/usr/bin/python3
"""
making_change module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount `total`.

    Args:
    coins (list): A list of integers representing the denominations
    of the available coins.
    total (int): The total amount of money for which change is to be made.

    Returns:
    int: The minimum number of coins needed to make up the total.
         Returns 0 if total is 0 or less.
         Returns -1 if it is not possible to make up the total 
         with the given coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
