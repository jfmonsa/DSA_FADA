from data_structures_implementation.linkedList import SingleLinkedListNode

"""
Approach
1 getSize of list
2 traverse until the lenght - k node: the next node goes Null and save the actual next node (new head in a temp var)
3 traverse until the last node and connect it to the given head

Little tip:
Module Operation:

k = k % length

is used to
+ manage efficiently cases where the number of rotations k is greater than the lenght of the list
    -> avoid unnecesary rotations
    -> Optimize the algo for big values of k

functioning:
+ if k < n, el the result will be k.
+ if k >= n, the result will be the effective number of rotations
"""


def rotateRight(head: SingleLinkedListNode, k: int) -> SingleLinkedListNode:
    # Edge cases
    if not head or not head.next:
        return head
    # find the length of the list
    n = 1
    curr = head
    while curr.next:
        curr = curr.next
        n += 1
    # set the tail of the list to point to the head
    curr.next = head
    # find the new head location
    k = k % n
    for _ in range(n - k):
        curr = curr.next
    # set the new head
    new_head = curr.next
    # set the new tail
    curr.next = None
    return new_head


if __name__ == "__main__":
    pass
