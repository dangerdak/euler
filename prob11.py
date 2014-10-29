# Project Euler Problem 11
# Largest product in a grid


def import_grid(input_file):
    """Return a list of lists, where each sublist is a row in the input_file."""
    input_list = []
    with open(input_file, 'r') as f:
        for line in f:
            new_line = line.split(' ')
            input_list.append([int(x) for x in new_line])
    return input_list


def list_product(my_list):
    """Return product of all values in my_list."""
    prod = 1
    for value in my_list:
        prod *= value
    return prod


def max_list_prod(n, my_list):
    """Return largest product of n consecutive numbers in my_list."""
    max_prod = 0
    prod = 1
    # Slicing exclusive of final index
    for index in range(len(my_list) - n + 1):
        prod = list_product(my_list[index:index + n])
        max_prod = max([max_prod, prod])
    return max_prod


def max_array_prod(n, my_array):
    """Return largest product of n consecutive numbers in my_array."""
    max_prod = 0
    for my_list in my_array:
        if len(my_list) >= n:
            print(len(my_list))
            prod = max_list_prod(n, my_list)
            max_prod = max([max_prod, prod])
    for my_list in transpose(my_array):
        if len(my_list) >= n:
            print(len(my_list))
            prod = max_list_prod(n, my_list)
            max_prod = max([max_prod, prod])
    for my_list in diagonals(my_array):
        if len(my_list) >= n:
            print(len(my_list))
            prod = max_list_prod(n, my_list)
            max_prod = max([max_prod, prod])
    return max_prod


def transpose(array):
    """Return transpose of array."""
    return [list(x) for x in zip(*array)]


def diagonals(array):
    """Return all diagonals of square array as lists."""
    # Assumes array is square
    length = len(array)
    new_array = []
    # LHS
    for diff in range(1, length):
        new_list = []
        for i in range(diff, length):
            new_list.append(array[i][i - diff])
        new_array.append(new_list)


    # RHS
    for diff in range(1, length):
        new_list = []
        for i in range(length-diff):
            new_list.append(array[i][i + diff])
        new_array.append(new_list)

    # Center
    new_list = []
    for i in range(length):
        new_list.append(array[i][i])
    new_array.append(new_list)

    # Minor center diagonal
    new_list = []
    j = length - 1
    for i in range(length):
        new_list.append(array[i][j])
        j -= 1
    new_array.append(new_list)

    # Minor LHS
    for max_index in range(length - 1, -1, -1):
        new_list = []
        j = max_index - 1
        for i in range(max_index):
            new_list.append(array[i][j])
            print(new_list)
            j -= 1
        new_array.append(new_list)

    # Minor RHS
    for min_index in range(1, length):
        new_list = []
        j = length - 1
        for i in range(min_index, length):
            new_list.append(array[i][j])
            j -= 1
        # TODO Why is an empty list added to the array?
        print(new_list)
        new_array.append(new_list)

    print(new_array)
    return new_array


if __name__ == '__main__':
    g = import_grid('grid-p11.txt')
    # g = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m = max_array_prod(4, g)

    print(m)
