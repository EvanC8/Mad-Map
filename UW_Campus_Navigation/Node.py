class Node:
    def __init__(self, node_id, lat, lon, g, h, adj_edges, parent_id=None):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon
        self.g = float('inf') if g is None else g
        self.h = 0 if h is None else h
        self.adj_edges = adj_edges
        self.parent_id = parent_id

    def f(self):
        return self.g + self.h