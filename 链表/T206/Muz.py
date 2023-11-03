from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            cur_tmp = cur.next
            pre_tmp = cur
            cur.next = pre
            cur = cur_tmp
            pre = pre_tmp
        return pre
