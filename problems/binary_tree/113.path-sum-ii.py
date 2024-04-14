# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        
        def tra(node, tsum, path):
            if not node: return
            
            path.append(node.val)
            if not node.left and not node.right and tsum == node.val:
                self.result.append(list(path))
                # return

            tra(node.left, tsum - node.val, path)
            
            tra(node.right, tsum - node.val, path)
            
            path.pop()
        
        tra(root, targetSum, [])
        
        return self.result