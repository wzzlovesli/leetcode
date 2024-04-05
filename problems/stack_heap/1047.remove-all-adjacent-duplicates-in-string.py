# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in s:
            if not stack or i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        
        return ''.join(stack)