# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def tra (node, ):
            if not node: return 0
            
            left_high = tra(node.left)
            right_high = tra(node.right)
            
            if left_high == -1 or right_high == -1:
                return -1
            
            if left_high - right_high in (0, -1, 1):
                return 1 + max(left_high, right_high)
            else:
                return -1
        
        return tra(root) != -1