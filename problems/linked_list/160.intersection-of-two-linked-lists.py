# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lens_a = 0
        
        index_a = headA
        while index_a:
            lens_a += 1
            index_a = index_a.next 
        
        lens_b = 0
        index_b = headB
        while index_b:
            lens_b += 1
            index_b = index_b.next
        
        cur_a, cur_b = headA, headB
        if lens_a > lens_b:
            cur_a, cur_b = cur_b, cur_a
            lens_a, lens_b = lens_b, lens_a
        
        for _ in range(lens_b - lens_a):
            cur_b = cur_b.next
        
        while cur_a:
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        
        return None