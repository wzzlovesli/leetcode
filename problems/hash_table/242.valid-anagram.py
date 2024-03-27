class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i_letter_count_arr = [0]*26
        for i in s:
            i_letter_count_arr[ord(i) - ord('a')] += 1
        
        for i in t:
            i_letter_count_arr[ord(i) - ord('a')] -= 1
            
        
        for i in i_letter_count_arr:
            if i != 0:
                return False
                
        return True