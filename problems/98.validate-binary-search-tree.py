from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid_bst(root, None, None)

    def is_valid_bst(self, root, min, max) -> bool:
        if root is None:
            return True
        
        if min is not None and root.val <= min.val:
            return False
        if max is not None and root.val >= max.val:
            return False
        
        return self.is_valid_bst(root.left, min, root) and self.is_valid_bst(root.right, root, max)

if __name__ == "__main__":
    print(Solution().isValidBST([2, 1, 3]))