# Definition for a binary tree node.
from typing import List, Optional
# Input: root = [1,null,2,3]
# Output: [1,2,3]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        
        # def traveral(node, result):
        #     if not node: return 
            
        #     result.append(node.val)
            
        #     traveral(node.left, result)
        #     traveral(node.right, result)
        
        # traveral(root, result)
        # return result
    
        # stack = [root]
        # result = []
        
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
            
        #     if node.right: stack.append(node.right)
        #     if node.left: stack.append(node.left)
        
        # return result

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if node:
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
        
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                result.append(node.val)
                
        return result