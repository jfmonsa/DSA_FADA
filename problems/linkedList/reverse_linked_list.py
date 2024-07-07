"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution
1. iterarative approach: time: O(n) ; memory: O(1)
2. recursive approach: time: O(n) ; memory: O(n) (Stack size)
"""

from typing import Optional
from data_structures_implementation.linkedList import (
    SingleLinkedListNode,
    SingleLinkedList,
)


# 1. Iterative approach
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


# 2. recursive approach
def reverseList2(head: Optional[SingleLinkedListNode]) -> Optional[SingleLinkedList]:
    return reverseList2_aux(head, None)


def reverseList2_aux(cur, prev):
    """
    Base case:
    if cur is None we are at the end of the list, the we return the prev which is
    our new head of the reversed list
    """
    if cur is None:
        return prev

    """
    Recursive case:
    We invert the link between the current_node
    """
    next = cur.next
    cur.next = prev
    return reverseList2_aux(next, cur)


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
    lst3 = SingleLinkedList()
    lst3.head = reverseList2(lst2.head)
    print(lst3)
