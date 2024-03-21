from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. simple
        # i = 0
        # arr_len = len(nums)

        # while i < arr_len:
        #     if nums[i] == val:
        #         for j in range(i + 1, arr_len):
        #             nums[j - 1] = nums[j]
            
        #         i -= 1
        #         arr_len -= 1
            
        #     i += 1
        
        # return arr_len
        
        
        # 2. 双指针-快慢
        # slow_index = 0
        # fast_index = 0
        # arr_len = len(nums)
        
        # while fast_index < arr_len:
        #     if nums[fast_index] != val:
        #         nums[slow_index] = nums[fast_index]
        #         slow_index += 1
            
        #     fast_index += 1
        
        # return slow_index
        
        
        # 3. 双指针-双向 3 2 2 3
        left_index = 0
        right_index = len(nums) - 1
        
        while left_index <= right_index:
            while left_index <= right_index and nums[left_index] != val:
                left_index += 1
            
            while left_index <= right_index and nums[right_index] == val:
                right_index -= 1
            
            if left_index < right_index:
                nums[left_index] = nums[right_index]
                left_index += 1
                right_index -= 1
            
        return left_index # 作为长度