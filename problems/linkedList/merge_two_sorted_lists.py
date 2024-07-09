from data_structures_implementation.linkedList import (
    SingleLinkedList,
    SingleLinkedListNode,
)
from typing import Optional

"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


def mergeTwoLists(
    list1: Optional[SingleLinkedListNode], list2: Optional[SingleLinkedListNode]
) -> Optional[SingleLinkedListNode]:

    dummy = SingleLinkedListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    while list1:
        tail.next = list1
        list1 = list1.next
        tail = tail.next

    while list2:
        tail.next = list2
        list2 = list2.next
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    # 1) Test case
    # [1,2,4]
    lst1 = SingleLinkedList()
    lst1.insertAtEnd(1)
    lst1.insertAtEnd(2)
    lst1.insertAtEnd(4)
    print(lst1)
    # [1,3,4]
    lst2 = SingleLinkedList()
    lst2.insertAtEnd(1)
    lst2.insertAtEnd(3)
    lst2.insertAtEnd(4)
    print(lst2)

    lst_result = SingleLinkedList()

    lst_result.head = mergeTwoLists(lst1.head, lst2.head)
    print(lst_result)
