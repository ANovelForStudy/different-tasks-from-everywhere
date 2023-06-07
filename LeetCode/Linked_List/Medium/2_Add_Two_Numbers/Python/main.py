

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = []
        second_list = []

        while l1:
            first_list.append(l1.val)
            l1 = l1.next

        while l2:
            second_list.append(l2.val)
            l2 = l2.next

        first_number = int("".join(map(str, first_list[::-1])))
        second_number = int("".join(map(str, second_list[::-1])))

        values = list(str(first_number + second_number))

        values = [int(i) for i in values[::-1]]

        head = ListNode(values[0])

        cur_node = head
        for i in values[1:]:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next

        return head
