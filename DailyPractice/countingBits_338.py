
import unittest
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [None]*(n+1)
        ans[0] = 0

        for k in range(1,n+1):
            i = k
            count = 0
            while i > 0:
                i =  i & (i-1)
                count += 1
                if ans[i]:
                    count += ans[i]
                    break
            ans[k] = count
        return ans

class TestCountBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: n = 2
        Output: [0, 1, 1]
        Explanation: 
        0 --> 0 (0 bits)
        1 --> 1 (1 bit)
        2 --> 10 (1 bit)
        """
        self.assertEqual(self.solution.countBits(2), [0, 1, 1])

    def test_example_2(self):
        """
        Input: n = 5
        Output: [0, 1, 1, 2, 1, 2]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
        """
        self.assertEqual(self.solution.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_zero(self):
        """
        Input: n = 0
        Output: [0]
        """
        self.assertEqual(self.solution.countBits(0), [0])

    def test_single_bit_boundary(self):
        """
        Input: n = 8 (a power of 2)
        Output: [0, 1, 1, 2, 1, 2, 2, 3, 1]
        """
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1]
        self.assertEqual(self.solution.countBits(8), expected)

    def test_large_n(self):
        """
        Test if the result for n=15 ends with 4 (binary 1111)
        """
        result = self.solution.countBits(15)
        self.assertEqual(len(result), 16)
        self.assertEqual(result[15], 4)

if __name__ == '__main__':
    unittest.main()