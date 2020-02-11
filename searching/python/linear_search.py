def linear_search(searchable_list, target):
    """
    Basic linear search implemented in python
    """

    for i in range(0, len(searchable_list)):
        if searchable_list[i] == target:
            return i

    return None
