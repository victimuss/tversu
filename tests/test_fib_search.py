import unittest
from src.fib_search import fibSearch

class TestFibSearch(unittest.TestCase):
    def test_elem_found(self):
        A = [3,4,7,10,13,16,18,19]
        self.assertEqual(fibSearch(A,8),[7,13,10,10])

    def test_not_in_range(self):
        A = [2, 4, 7, 9, 15]
        self.assertIsNone(fibSearch(A, 1))   # Меньше минимального
        self.assertIsNone(fibSearch(A, 20))  # Больше максимального

    def test_not_in_array(self):
        A = [2, 4, 6, 8, 10]
        self.assertEqual(fibSearch(A,5),[4,6])

    def test_critical_issues(self):
        A = []
        self.assertIsNone(fibSearch(A,5))

    def test_one_element(self):
        A = [7]
        self.assertEqual(fibSearch(A,7),[7])