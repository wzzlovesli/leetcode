# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    
    maxDepth = 0
        
    result = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        # que = deque([root])
        # result = 0
        # while que:
        #     nums = len(que)
        #     for i in range(len(que)):
        #         node = que.popleft()
                
        #         if i == 0: result = node.val
                
        #         if node.left: que.append(node.left)
        #         if node.right: que.append(node.right)
        # return result

        
        
        def tra(node, dep):
            if not node: return
            
            if dep > self.maxDepth:
                self.result = node.val
                
                self.maxDepth = dep
            
            if node.left: tra(node.left, dep + 1)
            
            if node.right: tra(node.right, dep + 1)
            
        tra(root, 1)
        
        return self.result
        
        
    
    
