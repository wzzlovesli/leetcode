# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        
        queue.append(root)
        
        result = []
        while queue:
            level = []
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                level.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            result.append(level)
            
        return result