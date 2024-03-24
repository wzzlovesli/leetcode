# Definition for singly-linked list.
from typing import Optional

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        pre_node = None
        cur_node = head
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            
            pre_node = cur_node
            cur_node = next_node
        
        return pre_node
        