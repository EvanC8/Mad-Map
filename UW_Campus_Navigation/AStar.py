import math
from parse_street_data import parse_street_data
from Priority_Queue import PriorityQueue
from MapVisualizer import MapVisualizer

# Finds the walkable path connecting two given intersections on UW-Madison campus
class AStar:
    def __init__(self):
        self.nodes, self.edges = parse_street_data()

        self.open_set = PriorityQueue(self.nodes, self.edges)
        self.closed_set = set()

        self.A = None
        self.B = None

        self.visualizer = MapVisualizer(self.nodes, self.edges)


    def find_path(self, start_node_id, end_node_id):
        self.A = start_node_id
        self.B = end_node_id

        start_node = self.nodes[start_node_id]
        start_node.g = 0

        self.open_set.enqueue(start_node_id)
        current = None

        print("Searching for path...")
        while True:
            if self.open_set.is_empty():
                break

            current_id = self.open_set.dequeue()
            current_node = self.get_node(current_id)

            if current_id == self.B:
                print("Path found!")
                path = self.reconstruct_path(current_node)
                print("Visualizing path...")
                self.visualizer.visualize(path, self.A, self.B)
                return

            self.closed_set.add(current_id)

            neighbors, lengths = self.get_neighbor_nodes(current_id)
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                length = lengths[i]

                tentative_g = current_node.g + length
                if tentative_g >= neighbor.g:
                    continue

                neighbor.parent_id = current_id

                old_f =  neighbor.f()
                neighbor.g = tentative_g
                # neighbor.h = self.heuristic(neighbor)

                if not self.open_set.contains(neighbor.node_id):
                    self.open_set.enqueue(neighbor.node_id)
                else:
                    if old_f != neighbor.f():
                        self.open_set.update_priority(neighbor.node_id, increase= (old_f < neighbor.f()))

        print("No path found.")
        return None


    def reconstruct_path(self, end_node):
        print("Reconstructing path...")
        path = []
        current = end_node
        while current is not None:
            path.append(current.node_id)
            current = self.get_node(current.parent_id) if current.parent_id else None

        print("Path from " + str(self.A) + " to " + str(self.B))
        print(path)
        return path[::-1]


    def get_neighbor_nodes(self, node_id):
        node = self.get_node(node_id)
        edge_ids = node.adj_edges

        neighbors = []
        lengths = []
        for edge_id in edge_ids:
            edge = self.edges[edge_id]
            node1_id = edge["node1"]
            node2_id = edge["node2"]
            length = edge["length"]

            if node_id == node1_id and node2_id is not None:
                neighbor_node = self.get_node(node2_id)
                neighbors.append(neighbor_node)
                lengths.append(length)
            elif node_id == node2_id and node1_id is not None:
                neighbor_node = self.get_node(node1_id)
                neighbors.append(neighbor_node)
                lengths.append(length)

        return neighbors, lengths


    def heuristic(self, node):
        R = 6371000

        lat1, lon1 = self.get_node(self.B).lat, self.get_node(self.B).lon
        lat2, lon2 = node.lat, node.lon

        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        dy = (lat2 - lat1) * 110540 * R
        dx = (lon2 - lon1) * math.cos((lat1 + lat2) / 2) * R

        return math.sqrt(dx ** 2 + dy ** 2)


    def get_node(self, node_id):
        return self.nodes[node_id]