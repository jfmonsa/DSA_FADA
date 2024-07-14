class BinaryTreeNode:
    def __init__(self, data, leftNode=None, rightNode=None) -> None:
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode


class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = BinaryTreeNode(root) if root is not None else None

    # height
    """
    Is like counting nodes to a leaf in the longest path
    """

    def height(self, root):
        # base case
        if root is None:
            return 0
        left_height = self.height(root.leftNode)
        right_height = self.height(root.rightNode)
        return max(left_height, right_height) + 1

    # depth: distance from root to current node

    # preorder print: time O(n) (n nodes);  space: O(n) (call stack)
    def print_preorder(self):
        lst = []
        self._print_preorder_aux(self.root, lst)
        return lst

    def _print_preorder_aux(self, node, lst):
        if node is not None:
            # node -> left -> right
            lst.append(str(node.data))
            self._print_preorder_aux(node.leftNode, lst)
            self._print_preorder_aux(node.rightNode, lst)
        # base case
        return


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
    # 1. tree_1 example:
    """
          1
        /   \
       2     3
      /
     4
    """
    tree_1 = BinaryTree(1)
    tree_1.root.leftNode = BinaryTreeNode(2)
    tree_1.root.rightNode = BinaryTreeNode(3)
    tree_1.root.leftNode.leftNode = BinaryTreeNode(4)
    print(tree_1.print_preorder())
    print(tree_1.height(tree_1.root))

    # 1. binary search tree
    bst_1 = BinarySearchTree(4)
    bst_1.insert(2)
    bst_1.insert_iterative(7)
    bst_1.insert(1)
    bst_1.insert(5)
    bst_1.insert(0)
    print(bst_1.print_preorder())
    print(bst_1.height(bst_1.root))
