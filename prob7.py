# Euler Project Problem 7
# 10001st prime number
from sys import argv


def is_prime(n, lesser_primes):
    """Returns true if n is a prime, otherwise false."""
    for divisor in lesser_primes:
        if n % divisor == 0:
            return False
    return True


def nth_prime(nth):
    """Returns nth prime number."""
    primes = [2]
    candidate = 3
    while len(primes) < nth:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 1
    return primes[-1]



if __name__ == '__main__':
    print(nth_prime(int(argv[1])))
