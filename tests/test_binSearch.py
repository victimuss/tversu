import unittest
from src.bins import binSearch

class TestBinSearch(unittest.TestCase):

    def test_element_found(self):
        A = [0, 2, 3, 8, 9, 10, 11, 14, 23, 28]
        self.assertEqual(binSearch(A, 11), [9, 14, 10, 11])

    def test_element_not_in_range(self):
        A = [2, 4, 7, 9, 15]
        self.assertIsNone(binSearch(A, 1))   # Меньше минимального
        self.assertIsNone(binSearch(A, 20))  # Больше максимального

    def test_empty_array(self):
        self.assertEqual(binSearch([], 5), [])

    def test_single_element(self):
        self.assertEqual(binSearch([5], 5), [5])
        self.assertIsNone(binSearch([5], 3))

    def test_multiple_cases(self):
        A = [2, 4, 7, 9, 15, 16, 20, 21, 22, 28, 29]
        self.assertEqual(binSearch(A, 13), [16, 7, 9, 15])

if __name__ == '__main__':
    unittest.main()
