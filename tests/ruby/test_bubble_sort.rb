require_relative "../../sorting/ruby/bubble_sort"
require "test/unit"


class TestBubbleSort < Test::Unit::TestCase

    def test_bubble_sort
        to_sort = [
            {sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9],
             unsorted: [9, 5, 6, 4, 2, 1, 3, 8, 7]},

            {sorted: [-100, 0, 32, 71, 3123, 93302, 12222222222222220],
             unsorted: [12222222222222220, 71, -100, 32, 0, 93302, 3123]
            },
            {
                sorted: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                unsorted: [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0]
            }
        ]
        to_sort.each do |item|
            arr = bubble_sort(item[:unsorted])
            assert_equal(item[:sorted], arr)
        end
    end
end
