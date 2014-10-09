# Euler Project Problem 7
# 10001st prime number
from sys import argv
import math


def is_prime(n):
    """Returns true if n is a prime, otherwise false."""
    # Ensure checks are made upto half of n
    limit = math.ceil(n/2) + 1
    # Plus one for cases when n = 2 or n = 4
    for divisor in range(2, limit):
        if n % divisor == 0:
            return False
    return True


def nth_prime(nth):
    """Returns nth prime number."""
    candidate = 1
    n_primes = 0
    while n_primes < nth:
        candidate += 1
        if is_prime(candidate):
            n_primes += 1
    return candidate



if __name__ == '__main__':
    print(nth_prime(int(argv[1])))
