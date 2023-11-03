from typing import Optional

"""
如果要操作一个节点一定要指向它前一个节点
"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next and cur.next.next:
            tmp_for_swap = cur.next
            tmp_for_move_cur = cur.next.next.next
            cur.next = tmp_for_swap.next
            cur.next.next = tmp_for_swap
            tmp_for_swap.next = tmp_for_move_cur
            cur = cur.next.next
        return dummy_head.next
