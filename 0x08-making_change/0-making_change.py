#!/usr/bin/python3
"""Define makeChange function."""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Return the fewest number of coins
    from `coins` list needed to meet `total`."""
    if total <= 0:
        return 0

    # start by the most valuable coin to achieve the fewest number of coins
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total:
            if total % coin == 0:
                # then use that coin denomination for the remaining total
                return count + total // coin

            # use the largest possible integer number of coins
            # from that coin denomination
            count += total // coin
            total = total % coin

    if total != 0:
        # then total cannot be met by any number of coins we have
        return -1

    return count
