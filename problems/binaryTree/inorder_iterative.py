"""
Given the root of a binary tree return the inorder
traversal of its nodes's values lists

Implement the algo iterative
"""

"""
Aproach:
+ Use a stack to manage and emulate recursive behaviour

Space: O(n), Time: O(n) (n is number of nodes)
"""

from data_structures_implementation.binaryTree import BinaryTreeNode
from typing import Optional


def inorder_iterative(root: Optional[BinaryTreeNode]) -> list[int]:
    lst = []
    stack = []
    """
    Tip: remember from the recursive approach
    inorder(root.left)
    proccess(root.data)
    inorder(root.right)
    """
    # pointer to the current node
    current_node = root
    while current_node or stack:
        while current_node:
            # go left as long as we can
            stack.append(current_node)
            current_node = current_node.leftNode
        current_node = stack.pop()
        lst.append(current_node.data)
        current_node = current_node.rightNode
    return lst


if __name__ == "__main__":
    # ex1
    """
           3
          / \
         9   20
            /  \
           15   7
    """
    root = BinaryTreeNode(3)
    root.leftNode = BinaryTreeNode(9)
    root.rightNode = BinaryTreeNode(20)
    root.rightNode.leftNode = BinaryTreeNode(15)
    root.rightNode.rightNode = BinaryTreeNode(7)
    print(inorder_iterative(root))
