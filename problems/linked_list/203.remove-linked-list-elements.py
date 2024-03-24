# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        virtual_node = ListNode(0, head)
        
        cur_node = virtual_node
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        
        return virtual_node.next