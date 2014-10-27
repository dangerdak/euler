# Euler Project Problem 10
# Summation of primes:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
from utils import timed


def is_prime(n):
    """Return true if n is a prime number"""
    # Skips for loop if n=2
    # Add one to limit for case when n=4
    for divisor in range(2, math.floor(math.sqrt(n) + 1)):
        if n % divisor == 0:
            return False
    return True


@timed
def sum_primes(limit):
    """Return sum of the primes below limit"""
    return sum(x for x in range(2, limit) if is_prime(x))


if __name__ == '__main__':
    print(sum_primes(10))
