# Input: ransomNote = "a", magazine = "b"
# Output: false


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        s_count = [0] * 26
        for s in magazine:
            s_count[ord(s) - ord('a')] += 1
            
        for s in ransomNote:
            s_count[ord(s) - ord('a')] -= 1

            if s_count[ord(s) - ord('a')] < 0:
                return False
        
        return True