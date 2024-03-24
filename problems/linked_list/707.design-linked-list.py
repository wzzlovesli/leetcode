class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur_node = self.dummy_head.next
        for _ in range(0, index):
            cur_node = cur_node.next
            
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        tmp_head = self.dummy_head.next
        self.dummy_head.next = ListNode(val, tmp_head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur_node = self.dummy_head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        cur_node = self.dummy_head
        for _ in range(index):
            cur_node = cur_node.next
        
        cur_node.next = ListNode(val, cur_node.next)
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur_node = self.dummy_head
        for _ in range(index):
            cur_node = cur_node.next
        
        cur_node.next = cur_node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)