# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        nums.sort()
        
        n = len(nums)
        
        for i in range(n):
            
            if nums[i] > target and nums[i] > 0 and target > 0:# 剪枝（可省）
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n): # 不可用enumerate, 生成的idx，每次都是从0开始的。
                
                if nums[i] + nums[j] > target and target > 0: #剪枝（可省）
                    break
                
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if  s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
        return result
                