# Ruby implementation of bubble sort.
# See documentation.needs.management/index.php/Sorting_Algorithms for
# the algorithm followed.

def bubble_sort(x)
    x = x[0,x.length()]
    x_range = *(0 ... x.length()-1)
    swapped = true
    while swapped
        swapped = false
        for y in x_range
            if x[y] > x[y+1]
                temp = x[y]
                x[y] = x[y+1]
                x[y+1] = temp
                swapped = true
            end
        end
    end
    return x
end
