from Heap import Heap

# Priority Queue built off of a min heap
class PriorityQueue:
    def __init__(self, nodes, edges):
        self.heap = Heap(nodes, edges)

    def enqueue(self, node_id):
        self.heap.insert(node_id)

    def dequeue(self):
        return self.heap.delete()

    def is_empty(self):
        return self.heap.size() == 0

    def size(self):
        return self.heap.size()

    def contains(self, node_id):
        return self.heap.contains(node_id)

    def node_index(self, node_id):
        return self.heap.index_of_node(node_id)

    def update_priority(self, node_id, increase):
        index = self.heap.index_of_node(node_id)
        if index is None:
            return

        if increase:
            self.heap.heapify_down(index)
        else:
            self.heap.heapify_up(index)
        return