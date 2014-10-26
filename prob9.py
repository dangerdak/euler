# Project Euler Problem 9
# Special Pythagorean Triplet


def pythag_triplet(total):
    for a in range(1, total + 1):
        for b in range(total - a, 0, -1):
            c = total - (a + b)
            if a**2 + b**2 == c**2:
                return a, b, c

if __name__ == '__main__':
    print(pythag_triplet(1000))
