
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_values(head):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        values = get_values(head)

        length = len(values)
        if length == 0:
            return None

        if length == 1:
            return ListNode(values[0])

        for i in range(0, length, 2):
            try:
                values[i], values[i+1] = values[i+1], values[i]
            except IndexError:
                break

        head = ListNode(values[0])
        cur = head
        for i in values[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return head


if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    solution = Solution()
    new_linked_list = solution.swapPairs(linked_list)

    cur = new_linked_list
    while cur:
        if cur.next:
            print(cur.val, end=" -> ")
        else:
            print(cur.val)
        cur = cur.next
    print()
