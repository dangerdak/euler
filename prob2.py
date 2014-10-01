# Project Euler Problem 2
# Even Fibonacci numbers


def sum_even_fib(limit):
    """Sum even fibonacci numbers upto max limit."""
    fib = [1, 2]
    while sum(fib[-2:]) < limit:
        fib.append(sum(fib[-2:]))
    fib_even = [x for x in fib if x % 2 == 0]
    return sum(fib_even)


if __name__ == '__main__':
    print(sum_even_fib(4000000))
