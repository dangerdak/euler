# Project Euler Problem 6
# Sum square difference

from sys import argv


def sum_squares(lower, upper):
    """Return the sum of the squares of the numbers between lower and upper."""
    total = 0
    # Don't use list comp as resulting list unneeded
    for i in range(lower, upper):
        total += i**2

    return total


def square_sum(lower, upper):
    """Return the square of the sum of the numbers between lower and upper."""
    total = sum(range(lower, upper))

    return total**2


def sum_square_diff(lower, upper):
    return square_sum(lower, upper) - sum_squares(lower, upper)


if __name__ == "__main__":
    print(sum_square_diff(int(argv[1]), int(argv[2])))
