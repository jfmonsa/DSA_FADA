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

    # TODO: depth: distance from root to current node

    # Depth-First Search Algos (DFS)
    # preorder
    def preorder_iterative(self):
        lst = []
        stack = []

        current_node = self.root
        while current_node or stack:
            while current_node:
                lst.append(current_node.data)
                stack.append(current_node)
                current_node = current_node.leftNode

            current_node = stack.pop()
            current_node = current_node.rightNode
        return lst

    def preorder(self):
        """
        preorder print: time O(n) (n nodes);  space: O(n) (call stack)
        """
        lst = []
        self._preorder_aux(self.root, lst)
        return lst

    def _preorder_aux(self, node, lst):
        if node is not None:
            # node -> left -> right
            lst.append(node.data)
            self._preorder_aux(node.leftNode, lst)
            self._preorder_aux(node.rightNode, lst)
        # base case
        return

    # inorder
    def inorder_iterative(self):
        lst = []
        stack = []
        # go to left
        current_node = self.root
        while current_node or stack:
            # go to left and add to stack
            while current_node:
                stack.append(current_node)
                current_node = current_node.leftNode
            current_node = stack.pop()
            lst.append(current_node.data)
            current_node = current_node.rightNode
        return lst

    def inorder(self):
        lst = []
        self._inorder_aux(self.root, lst)
        return lst

    def _inorder_aux(self, node, lst):
        if node is None:
            return
        self._inorder_aux(node.leftNode, lst)
        lst.append(node.data)
        self._inorder_aux(node.rightNode, lst)

    # postorder
    """
    There are 3 main approaches for an iterative postorder
    """

    # 1st approach: Using 2 stacks Time: O(n), O(n)
    def postorder_iterative_1(self):
        stack1 = [self.root]
        stack2 = []
        output = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.leftNode:
                stack1.append(node.leftNode)

            if node.rightNode:
                stack2.append(node.rightNode)

        while stack2:
            output.append(stack2.pop())

        return output

    # 2nd approach, using one stack and a prev pointer
    def postorder_iterative_2(self):
        stack = [self.root]
        prev = None
        output = []

        while stack:
            # stack.top()
            current_node = stack[-1]

            if (
                not prev
                or prev.leftNode == current_node
                or prev.rightNode == current_node
            ):
                if current_node.leftNode:
                    stack.append(current_node.leftNode)

                elif current_node.rightNode:
                    stack.append(current_node.rightNode)

            elif current_node.leftNode == prev:
                if current_node.rightNode:
                    stack.append(current_node.rightNode)

            else:
                output.append(current_node.data)
                stack.pop()

            prev = current_node
        return output


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
      / \   / \
     4   0  7  9
    """
    tree_1 = BinaryTree(1)
    tree_1.root.leftNode = BinaryTreeNode(2)
    tree_1.root.rightNode = BinaryTreeNode(3)
    tree_1.root.leftNode.leftNode = BinaryTreeNode(4)
    tree_1.root.leftNode.rightNode = BinaryTreeNode(0)
    tree_1.root.rightNode.leftNode = BinaryTreeNode(7)
    tree_1.root.rightNode.leftNode = BinaryTreeNode(9)
    print(tree_1.preorder())
    print(tree_1.preorder_iterative())
    print(tree_1.inorder())
    print(tree_1.inorder_iterative())
    print(tree_1.height(tree_1.root))

    # 1. binary search tree
    bst_1 = BinarySearchTree(4)
    bst_1.insert(2)
    bst_1.insert_iterative(7)
    bst_1.insert(1)
    bst_1.insert(5)
    bst_1.insert(0)
    print(bst_1.preorder())
    print(bst_1.height(bst_1.root))
