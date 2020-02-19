# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def select_sort(x):
    """
    A python implementation of select sort
    """

    x = x[:]

    for i in range(0, len(x)):
        temp = x[i]
        temp_index = i
        for j in range(i+1, len(x)):
            if x[j] < temp:
                temp = x[j]
                temp_index = j
        x[temp_index] = x[i]
        x[i] = temp

    return x
