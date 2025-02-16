import matplotlib.pyplot as plt
import networkx as nx

# Visualizes paths found using the AStar algorithm
class MapVisualizer:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def visualize(self, path=None, start_node_id=None, end_node_id=None):
        # Create graph object - NetworkX
        G = nx.Graph()

        # Add nodes and edges to the graph
        for node_id, node in self.nodes.items():
            G.add_node(node_id, pos=(node.lon, node.lat))

        for edge_id, edge in self.edges.items():
            node1_id = edge["node1"]
            node2_id = edge["node2"]
            G.add_edge(node1_id, node2_id, weight=edge["length"])

        # Get node positions for plotting
        pos = nx.get_node_attributes(G, 'pos')

        # Plot map - NetworkX
        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=False, node_size=5, node_color='blue', font_size=8, font_color='black')  # Smaller blue dots

        # Highlight start and end nodes
        if start_node_id:
            start_node = self.nodes[start_node_id]
            plt.plot(start_node.lon, start_node.lat, 'go', markersize=8)  # Start node in green
        if end_node_id:
            end_node = self.nodes[end_node_id]
            plt.plot(end_node.lon, end_node.lat, 'ro', markersize=8)  # End node in red

        # Overlay path
        if path:
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            for edge in path_edges:
                # Draw the path edges on top by calling plt.plot separately
                node1 = self.nodes[edge[0]]
                node2 = self.nodes[edge[1]]
                plt.plot([node1.lon, node2.lon], [node1.lat, node2.lat], color='orange', linewidth=3)

        # Show plot
        plt.title("UW-Madison Map with Path")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()
