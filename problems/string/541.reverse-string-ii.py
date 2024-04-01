# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Given a string s and an integer k, 
# reverse the first k characters for every 2k characters 
# counting from the start of the string.

# If there are fewer than k characters left, 
# reverse all of them. If there are less than 2k 
# but greater than or equal to k characters, 
# then reverse the first k characters and leave the other as original.


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def reverse(tmp):
            start_index = 0
            end_index = len(tmp) - 1
            
            while start_index < len(tmp) // 2:
                tmp[start_index], tmp[end_index] = tmp[end_index], tmp[start_index]
                
                start_index += 1
                end_index -= 1
            return tmp
        
        res = list(s)
        
        i = 0
        
        while i < len(res):
            # if i + k <= len(s):
            #     reverse(i, i+k)
            # else:
            #     reverse(i, len(s) -1)
            
            res[i: i+k] = reverse(res[i: i+k])
            
            # Written in this could be more pythonic.
            # s = s[:p] + s[p: p2][::-1] + s[p2:]
            i += 2*k
        
        return ''.join(res)