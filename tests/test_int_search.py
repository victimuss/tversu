import unittest
from src.intetpolsearch import interpolation_search

class TestIntSearch(unittest.TestCase):
    def test_element_found(self):
        A = [1, 4, 7, 8, 10, 17, 21, 23, 26, 32, 36, 40, 41, 43, 44, 47, 49]
        self.assertEqual(interpolation_search(A,8),[7,8])
    
    def test_element_not_in_range(self):
        A = [2, 4, 7, 9, 15]
        self.assertIsNone(interpolation_search(A, 1))   # Меньше минимального
        self.assertIsNone(interpolation_search(A, 20))  # Больше максимального

    def test_not_in_array(self):
        A = [2, 4, 6, 8, 10]
        self.assertEqual(interpolation_search(A,5),[6,4])
    
    def critical_issues(self):
        A = []
        self.assertEqual(interpolation_search(A,8),[])

    def one_element(self):
        A = [7]
        self.assertEqual(interpolation_search(A,7),[7])
    
    def incorrent(self):
        A = [1,2,3,1000]
        self.assertEqual(interpolation_search(A,4),[3,2])