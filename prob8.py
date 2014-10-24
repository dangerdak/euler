# Euler Project Problem 8
# Largest product in a series

def import_series(f):
    """
    Import file containing a series of numbers on different lines.
    Remove newlines and return string.
    """
    series = ''
    with open(f, 'r') as series_file:
        for line in series_file:
            series += line.strip('\n')
    return series


def max_product(n, n_adjacent):
    """Returns largest product of n_adjacent numbers within series n."""
    series = str(n)
    max_product = 0
    for index_start, start in enumerate(series):
        if index_start + n_adjacent > len(series) - 1:
            break
        product = int(start)
        for index_add in range(1, n_adjacent):
            product *= int(series[index_start + index_add])
        if product > max_product:
            max_product = product
    return max_product



if __name__ == '__main__':
    series = import_series('series.txt')
    print(max_product(series, 13))
