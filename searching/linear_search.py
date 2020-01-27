def linear_search(searchable_list, target):
    """
    Basic linear search implemented in python
    """

    for i in range(0, len(searchable_list)):
        if searchable_list[i] == target:
            return i

    return None

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

y = linear_search(x, 9)
print(y)
