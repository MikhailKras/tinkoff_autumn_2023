import unittest
from solution_sort import solution as func


class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(func(5, [1, 4, 2, 2, 4], [1, 4, 4, 2, 2]), "NO")

    def test_case2(self):
        self.assertEqual(func(6, [5, 1, 2, 5, 3, 5], [5, 1, 2, 3, 5, 5]), "YES")

    def test_case3(self):
        self.assertEqual(func(3, [4, 1, 2], [1, 4, 7]), "NO")

    def test_case4(self):
        self.assertEqual(func(1, [7], [7]), "YES")

    def test_case5(self):
        self.assertEqual(func(7, [4, 4, 1, 7, 5, 3, 8], [4, 1, 4, 5, 7, 3, 8]), "YES")

    def test_subseq_in_start(self):
        self.assertEqual(func(8, [8, 5, 7, 3, 8, 2, 9, 1], [5, 7, 8, 3, 8, 2, 9, 1]), "YES")

    def test_subseq_in_end(self):
        self.assertEqual(func(10, [2, 6, 1, 2, 3, 1, 7, 4, 9, 6], [2, 6, 1, 2, 3, 1, 4, 6, 7, 9]), "YES")

    def test_identical(self):
        self.assertEqual(func(7, [1, 8, 4, 5, 3, 9, 2], [1, 8, 4, 5, 3, 9, 2]), "YES")

    def test_full_seq(self):
        self.assertEqual(func(5, [2, 6, 1, 3, 2], [1, 2, 2, 3, 6]), "YES")

    def test_small_subseq(self):
        self.assertEqual(func(6, [5, 4, 5, 1, 4, 3], [5, 4, 1, 5, 4, 3]), "YES")


if __name__ == '__main__':
    unittest.main()
