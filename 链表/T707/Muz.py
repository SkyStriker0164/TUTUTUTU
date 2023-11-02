
"""
单链表设计
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class MyLinkedList:
    
    def __init__(self) -> None:
        self.dummy_head = ListNode()
        self.size = 0
    
    def get(self, index:int) -> int:
        pos = 0
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        while cur.next:
            if pos == index:
                break
            else:
                cur = cur.next
                pos += 1
        return cur.val
    
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val=val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.size += 1


    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val=val)
        new_node.next = None
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        pos = 0
        cur = self.dummy_head
        while cur:
            if pos == index:
                break
            else:
                cur = cur.next
                pos+=1
        cur.next = ListNode(val=val, next=cur.next)
        self.size += 1

    def deleteAtIndex(self, index:int) -> None:
        if index < 0 or index >= self.size:
            return
        pos = 0
        cur = self.dummy_head
        while cur.next:
            if pos == index:
                break
            else:
                cur = cur.next
                pos += 1
        cur.next = cur.next.next
        self.size -= 1




Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)


"""
双链表设计
"""

class ListNode:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self) -> None:
        self.head = ListNode()
        self.size = 0
    
    def get(self, index:int) -> int:
        pos = 0
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        while cur:
            if pos == index:
                break
            else:
                cur = cur.next
                pos += 1
        return cur.val
    
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val=val)
        new_node.next = self.head
        self.head.prev = new_node
        self.size += 1
    
    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val=val)
        new_node.next = None
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        self.size += 1
    
    def addAtIndex(self, index:int, val:int) -> None:
        if index < 0 or index > self.size:
            return
        pos = 0
        cur = self.head
        new_node = ListNode(val=val)
        while cur:
            if pos == index:
                break
            else:
                cur = cur.next
                pos += 1
        new_node.next = cur
        cur.prev = new_node
        self.size += 1
    
    def deleteAtIndex(self, index:int) -> None:
        pass

        