# Euler Project Problem 1
# Multiples of 3 and 5
import argparse


def sum_of_multiples(divisor1, divisor2, limit):
    """Find sum of all multiples of divisor1 or divisor2 below some limit."""
    multiples = []
    for n in range(1, limit):
        if (n % divisor1 == 0) or (n % divisor2 == 0):
            multiples.append(n)
    print(multiples)
    return sum(multiples)


def main():
    # Command line arguments determine
    # limit and divisors
    parser = argparse.ArgumentParser()
    parser.add_argument("divisor1",
                        type=int)
    parser.add_argument("divisor2",
                        type=int)
    parser.add_argument("limit",
                        help="limit below which multiples of divisor1 & \
                            divisor2 will be summed",
                        type=int)
    args = parser.parse_args()

    print(sum_of_multiples(args.divisor1, args.divisor2, args.limit))

if __name__ == '__main__':
    main()
