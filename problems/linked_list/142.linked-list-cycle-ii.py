# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_index = head
        slow_index = head
        
        while fast_index and fast_index.next:
            slow_index = slow_index.next
            fast_index = fast_index.next.next
            
            if slow_index == fast_index:
                slow_index = head
                
                while slow_index != fast_index:
                    slow_index = slow_index.next
                    fast_index = fast_index.next
                
                return slow_index
        
        return None