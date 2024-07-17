from .binaryTree import BinaryTree, BinaryTreeNode


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        self._insert_aux(value, self.root)
        return self.root

    """
    Recursive approach:
    Time complexity:
        O(h), h is height of the tree
        O(n) when h = n is the worst case (like linked list)

    Space:
        O(h) (callstack)
    """

    def _insert_aux(self, value, cur_node):
        # base case
        if cur_node is None:
            return BinaryTreeNode(value)
        # recurseive cases
        if value < cur_node.data:
            cur_node.leftNode = self._insert_aux(value, cur_node.leftNode)
        else:
            cur_node.rightNode = self._insert_aux(value, cur_node.rightNode)
        return cur_node

    """
    Iterative approach:
    time: O(n)
    space: O(1) (Only Pointers)
    """

    def insert_iterative(self, value):
        new_node = BinaryTreeNode(value)

        if self.root is None:
            self.root = new_node

        current_node = self.root
        while True:
            if value < current_node.data:
                if not current_node.leftNode:
                    current_node.leftNode = new_node
                    return
                current_node = current_node.leftNode
            else:
                if not current_node.rightNode:
                    current_node.rightNode = new_node
                    return
                current_node = current_node.rightNode


if __name__ == "__main__":
    # 1. binary search tree
    bst_1 = BinarySearchTree(4)
    bst_1.insert(2)
    bst_1.insert_iterative(7)
    bst_1.insert(1)
    bst_1.insert(5)
    bst_1.insert(0)
    print(bst_1.preorder())
    print(bst_1.height(bst_1.root))
