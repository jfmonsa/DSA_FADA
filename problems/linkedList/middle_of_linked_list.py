from typing import Optional
from data_structures_implementation.linkedList import SingleLinkedListNode

"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Approach:
+ two pointers fast (2x) / slow
+ if fast is at the tail, then slow will be at the middle
"""


def middleNode(head: Optional[SingleLinkedListNode]) -> Optional[SingleLinkedListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
