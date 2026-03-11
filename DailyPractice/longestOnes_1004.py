import unittest
from typing import List

class Solution:
   
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums) < k:
            return len(nums)
        
        if len(nums) == 0:
            return 0
        
        c = 0
        temp = 0

        for i in nums:
            if i == 1:
                temp += 1
            else:
                c = max(c,temp)
                temp = 0


        c = max(c,temp)

        if k == 0:
            return c


        if c != 0:
            i = 0
            j = c-1 
            ans = c

            z = 0
            p = 0
            while(p<c):
                if nums[p] == 0:
                    z += 1
                p += 1
            while(j < len(nums)):
                if z <= k:
                    ans = max(ans, j-i+1)
                    j += 1
                    if j< len(nums) and nums[j] == 0:
                        z += 1
                else:
                    if nums[i] == 0:
                        z -= 1
                    i += 1
            return ans
        
        else:
            return min(len(nums),k)
        






class TestLongestOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_k_larger_than_zeros(self):
        """
        Input: nums = [1,0,1,0,1], k = 3
        Output: 5
        """
        self.assertEqual(self.solution.longestOnes([1,0,1,0,1], 3), 5)

    def test_a_example_1(self):
        """
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6
        """
        self.assertEqual(self.solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)

    def test_example_2(self):
        """
        Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
        Output: 10
        """
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        self.assertEqual(self.solution.longestOnes(nums, 3), 10)

    def test_k_zero(self):
        """
        Input: nums = [1,1,0,1], k = 0
        Output: 2 (No flips allowed)
        """
        self.assertEqual(self.solution.longestOnes([1,1,0,1], 0), 2)

    def test_all_zeros_with_k(self):
        """
        Input: nums = [0,0,0,0], k = 2
        Output: 2
        """
        self.assertEqual(self.solution.longestOnes([0,0,0,0], 2), 2)

    def test_all_ones(self):
        """
        Input: nums = [1,1,1,1], k = 5
        Output: 4
        """
        self.assertEqual(self.solution.longestOnes([1,1,1,1], 5), 4)



    def test_single_element_zero_k_one(self):
        """
        Input: nums = [0], k = 1
        Output: 1
        """
        self.assertEqual(self.solution.longestOnes([0], 1), 1)

if __name__ == '__main__':
    unittest.main()