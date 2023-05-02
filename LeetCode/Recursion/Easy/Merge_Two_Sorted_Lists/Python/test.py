
from main import mergeTwoLists, ListNode


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

# Create the second linked list: 2 -> 4 -> NULL
list2 = ListNode(2)
list2.next = ListNode(4)

# Merge the two linked lists
merged = mergeTwoLists(list1, list2)

# Traverse the merged linked list and print its values
while merged:
    print(merged.val, end=" ")
    merged = merged.next
