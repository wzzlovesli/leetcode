from typing import List

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0

        next = self.get_next(needle)
        
        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            
            if haystack[i] == needle[j]:
                j += 1
                
            if j == len(needle):
                return i - len(needle) + 1
        
        return -1
            
            
    def get_next(self, needle: str) -> List[int]:
        next = [0] * len(needle)
        
        j = 0 
        next[0] = j
        
        for i in range(1, len(needle)):
            # 不相等
            while j > 0 and needle[i] != needle[j]:
                # 往前找j， 直到相等或者为0
                j = next[j - 1]
            
            # 相等
            if needle[i] == needle[j]:
                # j + 1
                j += 1
            # 赋值    
            next[i] = j
        
        return next
            
                    