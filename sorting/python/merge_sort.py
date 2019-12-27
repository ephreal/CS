# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.


def mergesort(x):
    if len(x) <= 1:
        return x
    x = x[:]
    # Split into smaller lists
    x, y = split(x)
    # Keep splitting
    x = mergesort(x)
    y = mergesort(y)
    # Merge lists together
    z = merge(x, y)
    return z

    return x


def split(x):
    split_index = (len(x)+1) // 2
    return [x[:split_index], x[split_index:]]


def merge(x, y):
    sorted = []
    for item in x:
        to_pop = []
        for j in y:
            if j <= item:
                sorted.append(j)
                to_pop.append(y.index(j))
            if j > item:
                break
        sorted.append(item)
        for i in reversed(to_pop):
            y.pop(i)
    if len(y):
        sorted.extend(y)
    return sorted


x = [7, 6, 2, 1, 3, 99, 103, -10, 0, 0, 9, 2, 9, 9, 9, 9, 3, 6, 9, 0, 102, -9]
y = mergesort(x)

print(x)
print(y)
