# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # result = []
        
        # def traversal(node, result):
        #     if not node: return 
            
        #     traversal(node.left, result)
        #     traversal(node.right, result)
        #     result.append(node.val)
            
        
        # traversal(root, result)
        
        # return result
        
        # result = []
        # stack = [root]
        
        # while stack:
        #     node = stack.pop()
        #     result.append(node)
            
        #     if node.left: stack.append(node.left)
        #     if node.right: stack.append(node.right)
        
        # return result[::-1]
        
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()

            if node:
                stack.append(node)
                stack.append(None)

                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
            else:
                node2 = stack.pop()
                result.append(node2.val)
        return result