# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 方式1
        # 遍历获取长度，
        # 计算倒数第n个的index
        # 重新遍历， 删除
        
        
        # 方式2
        # 定一个长度为n+1的数组，存放截止当前遍历的所有节点
        # 如果遍历结束，则删除数据第二个节点
        
        
        # 方式3
        # 双指针，快慢指针
        # 快指针比慢指针多走n+1
        # 快指针为结尾None时，慢指针为第n节点的上一个节点
        
        dummy_head = ListNode(0, head)
        
        slow_index = dummy_head
        fast_index = dummy_head
        
        for _ in range(n+1):
            fast_index = fast_index.next
        
        while fast_index:
            fast_index = fast_index.next
            slow_index = slow_index.next
            
        slow_index.next = slow_index.next.next
        
        return dummy_head.next