import unittest
from typing import List
from itertools import groupby

class Solution:
    def compress(self, chars: List[str]) -> int:

        read = 0
        write = 0
        count = 0


        return write+1


        

class TestCompress(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: chars = ["a","a","b","b","c","c","c"]
        Output: 6, chars[:6] = ["a","2","b","2","c","3"]
        """
        chars = ["a","a","b","b","c","c","c"]
        length = self.solution.compress(chars)
        self.assertEqual(length, 6)
        self.assertEqual(chars[:length], ["a","2","b","2","c","3"])

    def test_example_2(self):
        """
        Input: chars = ["a"]
        Output: 1, chars[:1] = ["a"]
        """
        chars = ["a"]
        length = self.solution.compress(chars)
        self.assertEqual(length, 1)
        self.assertEqual(chars[:length], ["a"])

    def test_example_3(self):
        """
        Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        Output: 4, chars[:4] = ["a","b","1","2"]
        """
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        length = self.solution.compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], ["a","b","1","2"])

    def test_no_repeats(self):
        """
        Input: chars = ["a","b","c"]
        Output: 3, chars[:3] = ["a","b","c"]
        """
        chars = ["a","b","c"]
        length = self.solution.compress(chars)
        self.assertEqual(length, 3)
        self.assertEqual(chars[:length], ["a","b","c"])

    def test_large_count(self):
        """
        Input: chars = ["a"] * 15
        Output: 3, chars[:3] = ["a","1","5"]
        """
        chars = ["a"] * 15
        length = self.solution.compress(chars)
        self.assertEqual(length, 3)
        self.assertEqual(chars[:length], ["a","1","5"])

    def test_mixed_case_and_symbols(self):
        """
        Input: chars = ["A","A","!","!","!"]
        Output: 4, chars[:4] = ["A","2","!","3"]
        """
        chars = ["A","A","!","!","!"]
        length = self.solution.compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], ["A","2","!","3"])

if __name__ == '__main__':
    unittest.main()