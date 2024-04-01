

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # abaaba
        # baab
        # aba
        # ss = (s + s)[1:-1]
        
        # return ss.find(s) != -1
        if len(s) == 0:
            return False
        
        next = self.get_next(s)
        
        if next[-1] != 0 and len(s) % (len(s) - next[- 1])  ==0:
            return True
        
        return False
    
    def get_next(self, s: str) -> List[int]:
        next = [0] * len(s)
        
        j = 0 
        next[0] = j
        
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]

            if s[i] == s[j]:
                j += 1
                
            next[i] = j
        
        return next
        