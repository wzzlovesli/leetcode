# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def tra(node, tsum):
            if not node: return False
            
            # tsum = tsum - node.val
            
            # if tsum < 0:
            #     return False

            # if tsum != 0 and not node.left and not node.right:
            #     return False
            
            if tsum == node.val and not node.left and not node.right:
                return True
            
            leftV = tra(node.left, tsum - node.val)
            
            rightV = tra(node.right, tsum - node.val)
            
            return leftV or rightV
        
        return tra(root, targetSum)
        