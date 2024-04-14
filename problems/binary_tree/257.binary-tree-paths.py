# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        def tra(node, path, result):
            path.append(str(node.val))
            
            if not node.left and not node.right:
                result.append('->'.join(path))
                
            if node.left:
                tra(node.left, path, result)
                path.pop()
            
            if node.right:
                tra(node.right, path, result)
                path.pop()
            
        tra(root, [], result)
        
        return result