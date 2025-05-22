from data_structures_implementation.heap import MinHeap

"""
Heapsort heapifies the array that we want to sort then
keeps extracting min until it becomes empty
"""

"""
time: O(n log(n))
space: O(n)
"""


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for _ in range(len(heap.nodes))]


if __name__ == "__main__":
    print(heapsort([99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]))

"""
+ In a priority queue elements has priority related
+ elements with the highest priority come at the front
+ to implement a P.Q. we use a MinHeap or MaxHeap
+ Operations in PQ:
    enequeue O(logn),
    dequeue O(long n),
    peek O(1),
    change priority O(log n) if we have the index else O(n),
    is_empy O(1)

PQ Applications
+ Dijkstra's algo
+ Huffman coding algo
+ Prim's algo
"""
