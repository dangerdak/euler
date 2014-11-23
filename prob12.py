# Project Euler Problem 12
# Highly divisible triangular number
# First to have over 500 divisors


def count_factors(n):
    """Return number of factors which n has, including 1 and itself."""
    # Add 1 to include n itself
    # count = len([d for d in range(1, (n+2)//2) if n % d == 0]) + 1
    # Divisors on LHS of number line
    factors = 0
    divisor = 1
    complement = n
    while divisor < complement:
        complement = n / divisor
        if complement.is_integer():
            factors += 2
        divisor += 1
    if divisor == complement:
        factors += 1
    return factors


def nth_triangle(n):
    """
    Return the nth triangular number.
    The nth triangular number is given by T = n(n+1)/2
    """
    triangle = n * (n + 1)//2
    return triangle


if __name__ == '__main__':
    i = 0
    while count_factors(nth_triangle(i)) < 500:
        i += 1

    print(nth_triangle(i))
