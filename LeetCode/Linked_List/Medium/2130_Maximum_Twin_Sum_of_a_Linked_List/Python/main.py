
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def get_values(head):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        values = get_values(head)
        length = len(values)

        max_ = -1
        for i_1, i_2 in zip(values[:length // 2], values[length // 2:][::-1]):
            sum_ = i_1 + i_2
            if sum_ > max_:
                max_ = sum_

        return max_


if __name__ == "__main__":
    solution = Solution()

    linked_list = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    max_sum = solution.pairSum(linked_list)
    print(max_sum)

    linked_list = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    max_sum = solution.pairSum(linked_list)
    print(max_sum)
