import unittest
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0

        while(read < len(nums)):


            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

            read += 1

        nums[write:] = [0]*(read-write)

        return nums

class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: nums = [0, 1, 0, 3, 12]
        Output: [1, 3, 12, 0, 0]
        """
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example_2(self):
        """
        Input: nums = [0]
        Output: [0]
        """
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_no_zeroes(self):
        """
        Input: nums = [1, 2, 3]
        Output: [1, 2, 3]
        """
        nums = [1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_all_zeroes(self):
        """
        Input: nums = [0, 0, 0]
        Output: [0, 0, 0]
        """
        nums = [0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_zeroes_at_end(self):
        """
        Input: nums = [1, 2, 0, 0]
        Output: [1, 2, 0, 0]
        """
        nums = [1, 2, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 0, 0])

    def test_negative_numbers(self):
        """
        Input: nums = [0, -1, 0, -3, 12]
        Output: [-1, -3, 12, 0, 0]
        """
        nums = [0, -1, 0, -3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, -3, 12, 0, 0])

    def test_single_non_zero(self):
        """
        Input: nums = [5]
        Output: [5]
        """
        nums = [5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [5])

if __name__ == '__main__':
    unittest.main()