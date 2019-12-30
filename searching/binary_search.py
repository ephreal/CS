# See documentation.needs.management/index.php/Search_Algorithms for
# the algorithm followed.


def binary_search(x, item):
    """
    Binary search implemented in python
    """

    # Start at the center of the search space (or as close as possible)
    highest = len(x)
    lowest = 0
    index = len(x)//2
    while not x[index] == item:
        if index < 0 or highest == lowest:
            # item not in the list
            return
        if x[index] < item:
            lowest = index
            mod = (highest - lowest)//2
            if mod == 0:
                # Item is above the range of the list
                return
            index += mod
        elif x[index] > item:
            highest = index
            index -= (highest) - (lowest)
    return index


def run_search(x, item):
    y = binary_search(x, item)
    if y is not None:
        print(f"Found at index {y}, x[{y}]: {x[y]}")
    else:
        print("Error, item not found")


x = [1, 2, 3, 4, 5]

for i in range(0, 7):
    run_search(x, i)
