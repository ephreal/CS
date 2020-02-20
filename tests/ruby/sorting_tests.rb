require_relative "../../sorting/ruby/bubble_sort"
require_relative "../../sorting/ruby/insert_sort"
require_relative "../../sorting/ruby/select_sort"
require "test/unit"


$sorts = [
            {
                sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9],
                unsorted: [9, 5, 6, 4, 2, 1, 3, 8, 7]
            },

            {
                sorted: [-100, 0, 32, 71, 3123, 93302, 12222222222222220],
                unsorted: [12222222222222220, 71, -100, 32, 0, 93302, 3123]
            },
            {
                sorted: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                unsorted: [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0]
            },
            {
                sorted: [-999, -999, -999, -999, -800, -799, -90, -1, 0, 0, 0,
                         0, 0, 1, 1, 1, 1, 4, 6, 8, 11, 34, 68, 68, 68, 68, 68,
                         68, 68, 68, 68, 99, 1024, 2221, 4129, 9123, 33213,
                         39013, 55421, 55421, 999999, 1000000],
                unsorted: [1000000, -999, 0, 68, 4129, 1, 0, 11, 68, 1, 4, 68,
                           -1, 39013, 68, 68, 8, 9123, 0, 1, 68, 1, 55421, 6,
                           68, -90, 0, -999, 999999, -799, 68, 2221, 99, -800,
                           -999, 55421, 0, 68, 33213, 1024, 34, -999]
            },
        ]

class TestBubbleSort < Test::Unit::TestCase

    def test_bubble_sort

        $sorts.each do |item|
            arr = bubble_sort(item[:unsorted])
            assert_equal(item[:sorted], arr)
        end
    end
end

class TestInsertSort < Test::Unit::TestCase

    def test_insert_sort
        $sorts.each do |item|
            arr = insert_sort(item[:unsorted])
            assert_equal(item[:sorted], arr)
        end
    end
end

class TestSelectSort < Test::Unit::TestCase

    def test_select_sort
        $sorts.each do |item|
            arr = select_sort(item[:unsorted])
            assert_equal(item[:sorted], arr)
        end
    end
end
