# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     arr = []
        
    #     def inorder(node):
    #         if not node:
    #             return
            
    #         inorder(node.left)
    #         arr.append(node.val)
    #         inorder(node.right)
        
    #     inorder(root)
    #     return arr
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        stack = []
        ans = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        
        return ans