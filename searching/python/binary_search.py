def binary_search(search_list, target):
    """"
    An implementation of a binary search in python.
    Returns the index in the list if the item is found. Returns None
    if not.
    """

    first = 0
    last = len(search_list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if search_list[midpoint] == target:
            return midpoint

        elif search_list[midpoint] < target:
            first = midpoint + 1

        elif search_list[midpoint] > target:
            last = midpoint - 1

    return None
