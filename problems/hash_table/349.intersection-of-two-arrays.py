from typing import List

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mark_table = {}

        for num in nums1:
            mark_table[num] = 1
        
        result_arr = set()
        for num in nums2:
            if num in mark_table.keys():
                result_arr.add(num)

                del mark_table[num]
            
        
        return result_arr