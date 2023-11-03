
"""
单链表设计
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# class MyLinkedList:
    
#     def __init__(self) -> None:
#         self.dummy_head = ListNode()
#         self.size = 0
    
#     def get(self, index:int) -> int:
#         pos = 0
#         if index < 0 or index >= self.size:
#             return -1
#         cur = self.dummy_head.next
#         while cur.next:
#             if pos == index:
#                 break
#             else:
#                 cur = cur.next
#                 pos += 1
#         return cur.val
    
#     def addAtHead(self, val:int) -> None:
#         new_node = ListNode(val=val)
#         new_node.next = self.dummy_head.next
#         self.dummy_head.next = new_node
#         self.size += 1


#     def addAtTail(self, val:int) -> None:
#         new_node = ListNode(val=val)
#         new_node.next = None
#         cur = self.dummy_head
#         while cur.next:
#             cur = cur.next
#         cur.next = new_node
#         self.size += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return
#         pos = 0
#         cur = self.dummy_head
#         while cur:
#             if pos == index:
#                 break
#             else:
#                 cur = cur.next
#                 pos+=1
#         cur.next = ListNode(val=val, next=cur.next)
#         self.size += 1

#     def deleteAtIndex(self, index:int) -> None:
#         if index < 0 or index >= self.size:
#             return
#         pos = 0
#         cur = self.dummy_head
#         while cur.next:
#             if pos == index:
#                 break
#             else:
#                 cur = cur.next
#                 pos += 1
#         cur.next = cur.next.next
#         self.size -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


"""
双链表设计
"""

class ListNode:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index:int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index < self.size // 2:
            cur = self.head
            for i in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size - index - 1):
                cur = cur.prev
        return cur.val
    
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val=val, prev=None, next=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1
    
    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val=val, prev=self.tail, next=None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1
    
    def addAtIndex(self, index:int, val:int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size // 2:
                cur = self.head
                for i in range(index - 1):
                    cur = cur.next 
            else:
                cur = self.tail
                for i in range(self.size - index):
                    cur = cur.prev
            new_node = ListNode(val=val, prev=cur, next=cur.next)
            cur.next.prev = new_node
            cur.next = new_node
            self.size += 1
    
    def deleteAtIndex(self, index:int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            if index  < self.size // 2:
                cur = self.head
                for i in range(index):
                    cur = cur.next
            else:
                cur = self.tail
                for i in range(self.size - index - 1):
                    cur = cur.prev
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        self.size -= 1
        