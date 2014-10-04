from sys import argv


def factors(n):
    """Returns a list of factors of n, excluding 1 and itself."""
    factors = [i for i in range(2, n) if n % i == 0]
    return factors


def largest_prime(l):
    """Returns the largest prime from a list of numbers l."""
    # Sort number from largest to smallest
    l.sort(reverse=True)
    for number in l:
        # If number has no factors then it's a prime
        if len(factors(number)) == 0:
            return number


if __name__ == '__main__':

    n = int(argv[1])

    factors_list = factors(n)
    print(factors_list)
    print(largest_prime(factors_list))
