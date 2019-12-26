# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def bubble_sort(x):
    """
    Bubble sort implemented in python
    """
    x = x[:]
    swaps = True

    while swaps:
        swaps = False
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                # Swap the items at these indexes
                temp = x[i+1]
                x[i+1] = x[i]
                x[i] = temp
                swaps = True

    return x


x = [7, 3, 1, 0, 77, 99, -123, 6543, -0]
y = bubble_sort(x)
print(y)
