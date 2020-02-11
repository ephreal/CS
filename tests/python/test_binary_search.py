from searching.python.binary_search import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.searches = [
            {'index': 0, 'item': 0, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 1, 'item': 1, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 2, 'item': 2, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 3, 'item': 3, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 4, 'item': 4, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 5, 'item': 5, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 6, 'item': 6, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 7, 'item': 7, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 8, 'item': 8, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 9, 'item': 9, 'list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {'index': 0, 'item': 0, 'list': [0, 10, 20, 30, 40, 50, 60, 70]},
            {'index': 4, 'item': 114, 'list': [0, 11, 15, 31, 114, 789, 900]},
        ]

    def test_binary_search(self):
        for i in self.searches:
            index = binary_search(i['list'], i['item'])
            self.assertEqual(i['index'], index)
