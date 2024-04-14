# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        def tra(node):
            if not node: return 0
            
            left = node.left
            right = node.right
            left_high = 1
            right_high = 1
            while left and right:
                left = left.left
                right = right.right
                
                left_high += 1
                right_high += 1
            
            if not left_high and not right_high:
                return (2 ** left_high) - 1
            
            left_high = tra(node.left)
            right_high = tra(node.right)
            
            return left_high + right_high + 1
            
        return tra(root)   