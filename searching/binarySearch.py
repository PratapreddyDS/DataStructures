from typing import List


# Recursive approach

class Solution:
    
    def bs(self, nums, target, start, end):
        
        if start >= end:
            if target == nums[end]:
                return end
            else:
                return -1
    
        mid = (start+end)//2
        
        if target == nums[mid]:
            return mid
        
        if target>nums[mid]:
            return self.bs(nums, target, mid+1, end)

        else:
            return self.bs(nums, target, start, mid)
        
            
    def search(self, nums: List[int], target: int) -> int:
        
        return self.bs(nums,target,0,len(nums)-1)


# Iterative approach

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        
        while(start <= end):
            
            if start == end:
                if target == nums[end]:
                    return end
                else:
                    return -1
                    
            mid = (start+end)//2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                start = mid+1
            else:
                end = mid


# testing

sol = Solution()
print('final solution : ',sol.search([-1,0,3,5,9,12],9))