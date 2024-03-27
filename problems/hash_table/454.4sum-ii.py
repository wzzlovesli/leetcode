# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0


from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 记录nums1 + nums2 结果 tmp_dict1 key为和，value为次数
        # 遍历nums3 + nums4 结果，是否和为0， 结果+1
        
        
        tmp_dict = {}
        for n1 in nums1:
            for n2 in nums2:
                tmp_dict[n1 + n2] = tmp_dict.get(n1 + n2, 0) + 1
        
        result = 0
        for n3 in nums3:
            for n4 in nums4:
                find_num = 0 - n3 - n4
                
                if find_num in tmp_dict:
                    result += tmp_dict[find_num]

        return result
        