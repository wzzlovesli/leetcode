from typing import List

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = []
        for idx, n in enumerate(nums):
            
            if n > 0: 
                return result
            
            if idx > 0 and n == nums[idx - 1]:
                continue
                
            left = idx + 1
            right = len(nums) - 1
            
            while left < right:
                sum = n + nums[left] + nums[right]
                
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    
                    # qu is
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
            
        return result
        
        