# Definition for singly-linked list.
from typing import Optional

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        
        pre_node = dummy_head
        cur_node = head
        while cur_node and cur_node.next:
            next_node = cur_node.next
            next_next_node = next_node.next
            
            pre_node.next = next_node
            next_node.next = cur_node
            cur_node.next = next_next_node
            
            pre_node = cur_node
            cur_node = next_next_node
        
        return dummy_head.next
        