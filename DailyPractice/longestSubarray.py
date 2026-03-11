import unittest
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        bz= 0
        ans = 0
        cnt = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                ans = max(ans,bz+cnt)
                bz = cnt
                cnt = 0
            elif nums[i] == 1:
                cnt += 1

        ans = max(ans, bz+cnt)

        if cnt == len(nums):
            return ans-1
        
        return ans


class TestLongestSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: nums = [1, 1, 0, 1]
        Output: 3
        """
        self.assertEqual(self.solution.longestSubarray([1, 1, 0, 1]), 3)

    def test_example_2(self):
        """
        Input: nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        Output: 5
        """
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        self.assertEqual(self.solution.longestSubarray(nums), 5)

    def test_example_3(self):
        """
        Input: nums = [1, 1, 1]
        Output: 2 (Must delete one element)
        """
        self.assertEqual(self.solution.longestSubarray([1, 1, 1]), 2)

    def test_all_zeros(self):
        """
        Input: nums = [0, 0, 0]
        Output: 0
        """
        self.assertEqual(self.solution.longestSubarray([0, 0, 0]), 0)

    def test_single_zero_between_ones(self):
        """
        Input: nums = [1, 0, 1, 1, 1, 0, 1]
        Output: 4
        """
        self.assertEqual(self.solution.longestSubarray([1, 0, 1, 1, 1, 0, 1]), 4)

    def test_no_ones(self):
        """
        Input: nums = [0, 0, 1, 0]
        Output: 1
        """
        self.assertEqual(self.solution.longestSubarray([0, 0, 1, 0]), 1)

    def test_multiple_zeros_consecutive(self):
        """
        Input: nums = [1, 1, 0, 0, 1, 1]
        Output: 2
        """
        self.assertEqual(self.solution.longestSubarray([1, 1, 0, 0, 1, 1]), 2)

    def test_empty_result_minimal_input(self):
        """
        Input: nums = [0]
        Output: 0
        """
        self.assertEqual(self.solution.longestSubarray([0]), 0)

if __name__ == '__main__':
    unittest.main()