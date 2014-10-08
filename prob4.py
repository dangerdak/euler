# Project Euler problem 4
# Largest palindrome made from the product of two numbers
# each with a user-determined number of digits

from sys import argv
import math


def is_palindrome(n):
    """Returns true if n is palindrome, else returns false."""
    n = str(n)
    # For odd lengths, no need to compare central digit
    limit = math.floor(len(n)/2)
    for i in range(limit):
        if n[i] != n[-i - 1]:
            return False
    return True


def products(n_digits):
    """Returns list of all multiples of two numbers with 'n_digits' digits."""
    n_digits = int(n_digits)
    lowest = int('1' + (n_digits - 1) * '0')
    greatest = int('1' + (n_digits) * '0')
    prods = []

    # Change j_max to avoid duplicate products
    # Like taking only the diagonal and below in a times table chart
    j_max = lowest

    for i in range(lowest, greatest):
        for j in range(lowest, j_max):
            prods.append(i*j)
        j_max += 1

    return prods


def largest_palindrome(ls):
    """Returns the largest palindromic number from a list 'ls'."""
    ls.sort(reverse=True)
    
    for n in ls:
        if is_palindrome(n):
            return n


if __name__ == '__main__':
    print(largest_palindrome(products(argv[1])))
