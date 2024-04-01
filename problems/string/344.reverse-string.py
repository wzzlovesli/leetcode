# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start_index = 0
        end_index = len(s) - 1
        
        while start_index < len(s) // 2:
            s[start_index], s[end_index] = s[end_index], s[start_index]
            
            start_index += 1
            end_index -= 1
            