# Min heap
class Heap:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.heap = []

    def contains(self, node_id):
        if self.size() == 0:
            return False

        index = self.locate_node(0, node_id)
        return False if index is None else True

    def index_of_node(self, node_id):
        if self.size() == 0:
            return None

        index = self.locate_node(0, node_id)
        return index

    def locate_node(self, i, goal_node_id):
        if i >= self.size():
            return None

        node_id = self.heap[i]

        if node_id == goal_node_id:
            return i

        if self.has_left_child(i):
            contains = self.locate_node(self.get_left_child_index(i), goal_node_id)
            if contains is not None:
                return contains

        if self.has_right_child(i):
            contains = self.locate_node(self.get_right_child_index(i), goal_node_id)
            if contains is not None:
                return contains

        return None

    def size(self):
        return len(self.heap)

    def insert(self, node_id):
        self.heap.append(node_id)
        self.heapify_up(self.size() - 1)

    def heapify_up(self, index):
        i = index
        while self.has_parent(i) and self.get_node(self.parent(i)).f() > self.get_node(self.heap[i]).f():
            self.swap(self.get_parent_index(i), i)
            i = self.get_parent_index(i)

    def get_node(self, node_id):
        return self.nodes[node_id]

    def delete(self):
        if self.size() == 0:
            return None

        root = self.heap[0]

        if self.size() > 1:
            self.heap[0] = self.heap.pop()
            self.heapify_down()
        else:
            self.heap.pop()

        return root

    def heapify_down(self, index=0):
        i = index

        while self.has_left_child(i):
            smaller_child_index = self.get_left_child_index(i)
            if self.has_right_child(i) and self.get_node(self.right_child(i)).f() < self.get_node(self.left_child(i)).f():
                smaller_child_index = self.get_right_child_index(i)
            if self.get_node(self.heap[i]).f() > self.get_node(self.heap[smaller_child_index]).f():
                self.swap(i, smaller_child_index)
            else:
                break
            i = smaller_child_index

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size()

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size()

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    @staticmethod
    def get_left_child_index(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child_index(index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


