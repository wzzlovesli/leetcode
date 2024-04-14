# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 0
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def tra(node,):
            if not node: return
            
            if node.left: tra(node.left)
            
            if node.right: tra(node.right)
            
            if node and node.left \
                and not node.left.left \
                and not node.left.right:
                self.result += node.left.val
                return 
            
        tra(root)
        
        return self.result