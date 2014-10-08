# Project Euler Problem 5
# Smallest common multiple of 1-20
from sys import argv
import numpy as np


def factorise(n):
    """Return a list of prime factors of n."""
    divisor = 2
    factors = []
    while divisor < n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
            divisor = 1
        divisor += 1
    factors.append(int(n))
    return factors


def freq_count(items):
    """Count frequency of items in a list. Return an item: count dictionary."""
    d = {}
    for item in items:
        d[item] = d.get(item, 0) + 1
    return d


def common_multiple(lower, upper):
    """Lower and upper define a range of numbers which are common factors."""
    max_occurences = {}
    for i in range(lower, upper):
        factors = factorise(i)
        occurences = freq_count(factors)
        for value, count in occurences.items():
            if count > max_occurences.get(value, 0):
                max_occurences[value] = count
    total = np.prod([value**count for value, count in max_occurences.items()])

    return total


if __name__ == "__main__":
    print(common_multiple(int(argv[1]), int(argv[2])))
