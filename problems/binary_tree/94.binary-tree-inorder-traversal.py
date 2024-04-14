# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root: return []
        
        # stack = []
        # ans = []
        # cur = root
        
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     ans.append(cur.val)
        #     cur = cur.right
        
        # return ans
        
        # result = []
        
        # def traveral(node, result):
        #     if not node: return 
            
        #     traveral(node.left, result)
        #     result.append(node.val)
        #     traveral(node.right, result)
        
        # traveral(root, result)
        
        # return result
        
        
        # result = []
        # stack = []
        # cur = root
        
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     node = stack.pop()
        #     result.append(node.val)
        #     cur = cur.right
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                if node.right: stack.append(node.right)
                
                stack.append(node)
                stack.append(None)
                
                if node.left: stack.append(node.left)
                
            else:
                node = stack.pop()
                result.append(node.val)
        
        return result