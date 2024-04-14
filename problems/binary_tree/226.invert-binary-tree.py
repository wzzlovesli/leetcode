# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # def invert(node):
        #     if not node: return
            
        #     invert(node.left)
        #     invert(node.right)

        #     node.left, node.right = node.right, node.left
        
        # invert(root)
        
        # return root
        
        
        # stack = [root]
        
        # while stack:
        #     node = stack.pop()
            
        #     node.left, node.right = node.right, node.left
            
        #     if node.left: stack.append(node.left)
        #     if node.right: stack.append(node.right)
        
        # return root
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                node.left, node.right = node.right, node.left
        