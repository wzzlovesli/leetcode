from typing import List

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_index, right_index = 0, 0
        lens_arr = len(nums) 
        
        sums = 0
        # min_lens = -1
        min_lens = float('inf')
        while right_index < lens_arr: #  and left_index < lens_arr
            sums += nums[right_index]
            
            # if sums >= target:
            #     if min_lens == -1 or min_lens > right_index - left_index + 1:
            #         min_lens = right_index - left_index + 1
                
            #     sums -= nums[left_index]
            #     sums -= nums[right_index]
            #     left_index += 1
            # else:
            #     right_index += 1
            
            while sums >= target:
                # if min_lens == -1 or min_lens > right_index - left_index + 1:
                #     min_lens = right_index - left_index + 1
                min_lens = min(min_lens, right_index - left_index + 1)
                sums -=  nums[left_index]
                left_index += 1
            
            right_index += 1
        
        return min_lens if min_lens != float('inf') else 0
            
        
            