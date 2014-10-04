from sys import argv


def greatest_prime_factor(n):
    """Returns greatest prime factor of n. If n is prime, returns n."""
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            n = n / divisor
            divisor = 1
        # Python doesn't have an increment operator!
        divisor += 1
    return n


if __name__ == '__main__':
    print(greatest_prime_factor(int(argv[1])))
