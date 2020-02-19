from sorting.python.merge_sort import mergesort
import unittest


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.sorts = [
                        {
                            'sorted': [0, 1, 1, 1, 3, 3, 4, 4, 6, 9, 9310],
                            'unsorted': [9, 3, 4, 1, 6, 0, 4, 1, 3, 1, 9310]
                        },
                        {
                            'sorted': [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                            'unsorted': [0, 9, -1, 3, 2, 5, 7, 4, 6, 8, 1]
                        },
                        {
                            'sorted': [-10, -9, 0, 0, 0, 1, 2, 2, 3, 3, 6, 6,
                                       7, 9, 9, 9, 9, 9, 9, 99, 102, 103],
                            'unsorted': [7, 6, 2, 1, 3, 99, 103, -10, 0, 0, 9,
                                         2, 9, 9, 9, 9, 3, 6, 9, 0, 102, -9]
                        },
                        {
                            'sorted': [-9029, -9000, -1, 1, 4, 6029],
                            'unsorted': [-9000, 6029, 4, 1, -1, -9029]
                        }

                     ]

    def test_mergesort(self):
        for i in self.sorts:
            sorted = mergesort(i['unsorted'])
            self.assertEqual(i['sorted'], sorted)
