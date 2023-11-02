from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode: 
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        创建虚拟头节点让链表统一删除规则
        """
        fake_head = ListNode()
        fake_head.next = head
        pnt = fake_head
        while pnt.next:
            if pnt.next.val == val:
                pnt.next = pnt.next.next
            else:   
                pnt = pnt.next
        return fake_head.next
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.removeElements([1,2,6,3,4,5,6], 6))
