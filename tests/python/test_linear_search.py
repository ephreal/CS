from searching.python.linear_search import linear_search
import unittest


class TestLinearSearch(unittest.TestCase):
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
            {'index': 7, 'item': 0, 'list': [1, 2, 3, 4, 5, 6, 7, 0, 8, 9]},
            {'index': 9, 'item': 3, 'list': [0, 1, 2, 4, 5, 6, 7, 8, 9, 3]},
            {'index': 5, 'item': 1, 'list': [0, 2, 3, 4, 5, 1, 6, 7, 8, 9]},
            {'index': 4, 'item': 8, 'list': [0, 1, 2, 3, 8, 4, 5, 6, 7, 9]},
            {'index': 6, 'item': 0, 'list': [32, 12, 8, 111, 324, 3, 0, 6]},
        ]

    def test_linear_search(self):
        for i in self.searches:
            index = linear_search(i['list'], i['item'])
            self.assertEqual(i['index'], index)
