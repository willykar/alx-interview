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

    sorted_coins = sorted(coins, reverse=True)
    coin_length = len(coins)
    coin_position = 0
    count = 0

    while total > 0:
        if coin_position >= coin_length:
            return -1
        if total - sorted_coins[coin_position] >= 0:
            total -= sorted_coins[coin_position]
            count += 1
        else:
            coin_position += 1
    return count
