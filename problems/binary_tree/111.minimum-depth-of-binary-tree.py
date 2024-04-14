# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # result = float('inf')
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # postorder high
        # def dep(node, high):
        #     if not node: return 0
            
        #     left_high = dep(node.left)
        #     right_high = dep(node.right)
            
        #     if node.left and not node.right:
        #         return 1 + left_high
            
        #     if node.right and not node.left:
        #         return 1 + right_high

        #     return 1 + min(left_high, right_high)
        
        # return dep(root)
        
        # preorder dep
        # if not root: return 0
        
        # def dep(node, dp):
        #     if not node.left and not node.right:
        #         # global result
        #         self.result = min(self.result, dp)
            
        #     if node.left: dep(node.left, dp+1)
        #     if node.right: dep(node.right, dp+1)
            
        # dep(root, 1)
        # return self.result
        
        # 层序遍历
        
        if not root: return 0
        que = deque()
        
        que.append(root)
        result = 0
        while que:
            result += 1
            for _ in range(len(que)):
                node = que.popleft()
                if not node.left and not node.right:
                    return result
            
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        return result