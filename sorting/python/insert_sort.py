# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def insert_sort(x):
    """
    A python implementation of insert sort.
    """

    x = x[:]
    # Start from index 1 as index 0 is considered sorted already
    for i in range(1, len(x)):
        value = x[i]
        x.pop(i)
        while (i > 0 and x[i-1] > value):
            i -= 1
        x.insert(i, value)

    return x
