# Project Euler Problem 9
# Special Pythagorean Triplet
from utils import timed


@timed
def pythag_triplet(total):
    for a in range(1, total + 1):
        for b in range(total - a, 0, -1):
            c = total - (a + b)
            if a**2 + b**2 == c**2:
                return a, b, c


def product(*args):
    prod = 1
    for value in args:
        prod *= value
    return prod

if __name__ == '__main__':
    print(product(*pythag_triplet(1000)))
