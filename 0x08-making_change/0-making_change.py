#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    dp = 0
    tmp = 0
    coins.sort(reverse=True)
    for coin in coins:
        while dp < total:
            dp += coin
            tmp += 1
        if dp == total:
            return tmp
        dp -= coin
        tmp -= 1
    return -1
