from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self) -> str:
        return f'val: {self.val}, left: {self.left}, right: {self.right}'
    
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        def generateTree(start, end):
            print(f'start is: {start}, end is: {end}')
            if start > end:
                print(f'returning [None]')
                return [None]
            res = []
            for i in range(start, end + 1):
                print(f'i is: {i}')
                ls = generateTree(start, i - 1)
                rs = generateTree(i + 1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        print(f'node is: {node}')
                        res.append(node)

            return res

        return generateTree(1, n)

if __name__ == "__main__":
    print(Solution().generateTrees(3))
    