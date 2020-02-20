# Insert sort is an in place sorting method that builds a sorted list at the
# beginning of the list it sorts. Everything is sorted relative to that item.

def insert_sort(x)

    insert_point = 0

    (1..x.length()-1).to_a.each do |index|

        item = x[index]
        x.delete_at(index)

        while (x[insert_point] <= item) and (insert_point < index)
            insert_point += 1
        end

        x.insert(insert_point, item)

        insert_point = 0
    end

    return x
end
