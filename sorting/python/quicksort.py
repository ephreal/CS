# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def quicksort(x):
    """
    Sorts a list of integers using the quicksort algorithm. No special care
    was taken to ensure this is super efficient or even coded super well.
    """
    x = x[:]
    if len(x) <= 1:
        return x

    # Set the pivot to the last element in the list
    pivot = x[-1]
    x.pop(-1)
    larger = []
    smaller = []

    for i in x:
        if i <= pivot:
            smaller.append(i)
        if i > pivot:
            larger.append(i)

    # That's right, time for some recursion!
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    smaller.append(pivot)
    smaller.extend(larger)
    return smaller

    return x
