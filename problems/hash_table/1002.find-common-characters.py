# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count_arr = [0]* 26
        for i in words[0]:
            count_arr[ord(i)- ord('a')] += 1
        
        for word in words[1:]:
            count_tmp_arr = [0] * 26
            for i in word:
                count_tmp_arr[ord(i) - ord('a')] += 1
            
            for i in range(26):
                count_arr[i] = min(count_arr[i], count_tmp_arr[i])
        
        result_arr = []
        for i, v in enumerate(count_arr):
            while v:
                result_arr.append(chr(i + ord('a')))
                v -= 1
        
        return result_arr