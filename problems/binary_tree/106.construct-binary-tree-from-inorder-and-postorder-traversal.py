# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not postorder: return 
        
        root = postorder[-1]
        root_node = TreeNode(root)
        
        def tra(inorder: List[int], postorder: List[int], root):
            
            if not postorder: return 
            
            if len(postorder) == 1 : return
            
            root_val = postorder[-1]
            
            idx = inorder.index(root_val)
            
            left_inorder = inorder[0:idx]
            left_postorder = postorder[0:idx]
            left_node = TreeNode(left_postorder[-1])
            root.left = left_node
            
            tra(left_inorder, left_postorder, left_node)
            
            if idx < len(inorder) and idx >= 1: 
                right_inorder = inorder[idx+1:]
                right_postorder = postorder[len(left_inorder)-1:-2]
                right_node = TreeNode(right_postorder[-1])
                root.right = right_node
                tra(right_inorder, right_postorder, right_node)
        
        tra(inorder, postorder, root_node)
        
        return root_node
            