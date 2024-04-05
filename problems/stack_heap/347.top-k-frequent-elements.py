
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 遍历所有元素获取元素量级
        num_count = {}
        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1
        
        # 排序+TOPk， K大小的小顶堆，
        pri_que = []
        
        for key, freq in num_count.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
            
        # 输出
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        
        return result