# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        flag = True
        def isSym(left_node, right_node):
            if not left_node and not right_node: return True
            elif left_node and not right_node: return False
            elif right_node and not left_node: return False
            elif left_node.val != right_node.val: return False
            
            return isSym(left_node.right, right_node.left) and isSym(left_node.left, right_node.right)
        
        return isSym(root.left, root.right)