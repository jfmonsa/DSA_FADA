class BinaryTreeNode:
    def __init__(self, data, leftNode=None, rightNode=None) -> None:
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode


class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = BinaryTreeNode(root) if root is not None else None

    # height

    # level of a given node in tree

    # search node in tree

    # preorder print: time O(n) (n nodes);  space: O(n) (call stack)
    def print_preorder(self):
        lst = []
        self._print_preorder_aux(self.root, lst)
        return lst

    def _print_preorder_aux(self, node, lst):
        if node is not None:
            # Root -> left -> right
            lst.append(str(node.data))
            self._print_preorder_aux(node.leftNode, lst)
            self._print_preorder_aux(node.rightNode, lst)
        # base case
        return


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
