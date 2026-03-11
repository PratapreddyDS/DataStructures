import unittest
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [1, 2, 7, 4, 3, 1]

        i = len(nums)-2
        j = len(nums)-1

        breakPoint = -1

        while(i>=0):

            if nums[i] < nums[j]:
                breakPoint = i
                break

            
            j -= 1
            i -= 1

        if i == len(nums)-2 and j == len(nums)-1:
            nums[j] , nums[i] = nums[i], nums[j]
            return nums

        
        if breakPoint != -1:

            element = nums[breakPoint]
            nextGreater = float('inf')
            nextGreaterIndex = -1

            k = len(nums)-1

            while(k>=breakPoint):

                if nextGreater >= nums[k] > element:
                    nextGreater = nums[k]
                    nextGreaterIndex = k

                k -= 1

            nums[breakPoint], nums[nextGreaterIndex] = nums[nextGreaterIndex], nums[breakPoint]

            # nums1 = nums

            nums[breakPoint+1:] = sorted(nums[breakPoint+1:])

            return nums


        else:
            return nums.sort()






class TestNextPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_2(self):
        """
        Input: nums = [1, 2, 3]
        Output: [1, 3, 2]
        """
        nums = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_an_example_1(self):
        """
        Input: nums = [5,4,7,5,3,2]
        Output: [5,5,2,3,4,7]
        """
        nums = [2,3,1,3,3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums,[2,3,3,1,3])

    def test_example_3(self):
        """
        Input: nums = [1, 1, 5]
        Output: [1, 5, 1]
        """
        nums = [1, 1, 5]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])

    def test_single_element(self):
        """
        Input: nums = [1]
        Output: [1]
        """
        nums = [1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1])

    def test_duplicate_elements(self):
        """
        Input: nums = [1, 5, 1]
        Output: [5, 1, 1]
        """
        nums = [1, 5, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [5, 1, 1])

    def test_complex_case(self):
        """
        Input: nums = [1, 3, 5, 4, 2]
        Output: [1, 4, 2, 3, 5]
        """
        nums = [1, 3, 5, 4, 2]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 4, 2, 3, 5])

    def test_partially_decreasing(self):
        """
        Input: nums = [2, 3, 1]
        Output: [3, 1, 2]
        """
        nums = [2, 3, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [3, 1, 2])

    def test_partially_increasing_at_end(self):
        """
        Input: nums = [2, 1, 3]
        Output: [2, 3, 1]
        """
        nums = [2, 1, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [2, 3, 1])


if __name__ == '__main__':
    unittest.main()