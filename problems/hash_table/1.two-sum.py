# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_index = {}
        for idx, num in enumerate(nums):
            find_num = target - num
            
            if find_num in num_index:
                return [idx, num_index[find_num]]
            
            if num not in num_index:
                num_index[num] = idx
        
        return []