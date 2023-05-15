
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_values(head):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        values = get_values(head)

        values[k-1], values[-k] = values[-k], values[k-1]

        head = ListNode(values[0])
        cur = head
        for i in values[1:]:
            cur.next = ListNode(i)
            cur = cur.next

        return head
