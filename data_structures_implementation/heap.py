class MinHeap:
    """
    Abstracting the node data as Int but could be Any, given a custom comparison
    function to guide ourselves on how to compare the nodes.
    """

    # build minHeap (min heapify)
    # time: O(n) (long mathematical demostration)
    # => T(n) = 0*n/2 + 1+n/4 + 2*n/8 + 3*n/16 + ... + (lg(n-1)*n/n)

    def __init__(self, arr=None):
        self.nodes = []
        if type(arr) is list:
            self.nodes = arr.copy()
            # we begin in n // 2 because we only can do
            # siftdown in non-leaf nodes
            for i in range(len(self.nodes) // 2, -1, -1):
                self._siftdown(i)

    # insertion & update O(lg(n))
    def insert(self, element):
        self.nodes.append(element)
        self._siftup(len(self.nodes) - 1)

    def update_by_index(self, i, new_elm):
        old = self.nodes[i]
        self.nodes[i] = new_elm
        if new_elm < old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.nodes:
            self.update_by_index(self.nodes.index(old), new)

    # pop (extract) O(lg(n))
    def pop(self):
        pass

    # extract min O(lg(n))
    """
    Swap the peek with the last element and siftdown
    """

    def extract_min(self):
        if len(self.nodes) == 0:
            return None
        minval = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()
        self._siftdown(0)
        return minval

    # heap peek O(1)
    def peek(self):
        "get min"
        return self.nodes[0] if len(self.nodes) > 0 else None

    # aux operations
    """
    O(lg(n))
    Keep swapping the node with its children when they're smaller
    + if both are smaller we swap with the smaller one
    """

    def _siftdown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        while (left < len(self.nodes) and self.nodes[i] > self.nodes[left]) or (
            right < len(self.nodes) and self.nodes[i] > self.nodes[right]
        ):
            smallest = (
                left
                if (right >= len(self.nodes)) or self.nodes[left] < self.nodes[right]
                else right
            )
            self.nodes[i], self.nodes[smallest] = self.nodes[smallest], self.nodes[i]
            i = smallest
            left = 2 * i + 1
            right = 2 * i + 2

    """
    O(lg(n))
    Keep swapping the node with its parent if it is smaller
    """

    def _siftup(self, i):
        parent = (i - 1) // 2
        while i != 0 and self.nodes[parent] > self.nodes[i]:
            self.nodes[parent], self.nodes[i] = self.nodes[i], self.nodes[parent]
            i = parent
            parent = (i - 1) // 2
