"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional
from data_structures_implementation.linkedList import (
    SingleLinkedListNode,
    SingleLinkedList,
)


def reverseList(head: Optional[SingleLinkedListNode]) -> Optional[SingleLinkedListNode]:
    # two pointers
    prev = None
    head

    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev


if __name__ == "__main__":
    # Ex1: reverse 1->2->3->4->5->null
    lst1 = SingleLinkedList()
    lst1.insertAtEnd(1)
    lst1.insertAtEnd(2)
    lst1.insertAtEnd(3)
    lst1.insertAtEnd(4)
    lst1.insertAtEnd(5)
    lst2 = SingleLinkedList()
    lst2.head = reverseList(lst1.head)
    print(lst2)
