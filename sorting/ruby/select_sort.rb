# select sort
# An in place sorting method that selects the correct item from the unsorted
# part of the list and places it at the end of the sorted section of the list.

def select_sort(x)

    smallest = 0

    x.length().times do |index|
        smallest = index
        (index..x.length()-1).each do |check|
            if x[check] < x[smallest]
                smallest = check
            end
        end
        temp = x[index]
        x[index] = x[smallest]
        x[smallest] = temp
    end

    return x
end
