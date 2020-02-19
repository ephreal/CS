# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def mergesort(x):
    """
    Mergesort implemented in python.
    """
    if len(x) == 1:
        return x

    sorted = []
    curr_first = 0
    curr_last = 0

    first = mergesort(x[:len(x)//2])
    last = mergesort(x[len(x)//2:])

    while not curr_first == len(first):
        try:
            while last[curr_last] <= first[curr_first]:
                sorted.append(last[curr_last])
                curr_last += 1
        except IndexError:
            pass
        sorted.append(first[curr_first])
        curr_first += 1

    if not curr_last == len(last):
        sorted.extend(last[curr_last:])

    return sorted
