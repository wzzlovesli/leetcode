from typing import List

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lens_arr = len(nums)
        
        left_index = 0
        right_index = lens_arr - 1
        
        # result_arr = [0 for _ in nums]
        result_arr = [float('inf')] * lens_arr
        result_index = lens_arr - 1
        while left_index <= right_index:
            if nums[left_index]*nums[left_index] >= nums[right_index]*nums[right_index]:
                result_arr[result_index] = nums[left_index]*nums[left_index]
                left_index += 1
            else:
                result_arr[result_index] = nums[right_index]*nums[right_index]
                right_index -= 1
            
            result_index -= 1
        
        return result_arr
            