# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.



from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        next = [0]*len(needle)
        self.get_next(next, needle)
        
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            
            if haystack[i] == needle[j]:
                j += 1
            
            if j == len(needle):
                return i - len(needle) + 1
            
        return -1
        
    def get_next(self, next_list: List[int], needle):
        j = 0
        next_list[0] = j
        
        for i in range(1, len(needle)):
            # 不相等
            while j > 0 and needle[i] != needle[j]:
                j = next_list[j-1]
            
            # 相等
            if needle[i] == needle[j]:
                j += 1
            
            # 赋值
            next_list[i] = j
            
            
            
            