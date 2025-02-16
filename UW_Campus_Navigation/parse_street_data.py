from Node import Node
import pandas as pd

def parse_street_data():
    # Load CSVs
    nodes_df = pd.read_csv("uw_madison_nodes.csv", index_col='node_id')
    edges_df = pd.read_csv("uw_madison_edges.csv", index_col='edge_id')

    # Initialize dictionaries
    nodes = {}
    edges = {}

    # Populate nodes dictionary
    for index, row in nodes_df.iterrows():
        # Parse adjacent edges list
        adj_edges = [int(x) for x in row['neighbor_edges'].split(";")] if pd.notna(row['neighbor_edges']) else []
        # Insert node
        # nodes[index] = {'id': index, 'lat': row['lat'], 'lon': row['lon'], 'adj_roads': adj_edges}
        nodes[index] = Node(index, row['lat'], row['lon'], None, None, adj_edges, None)

    print("Loaded all nodes")

    # Populate roads dictionary
    for index, row in edges_df.iterrows():
        # Insert edge
        edges[index] = {'id': index, 'length': row['length'], 'node1': row['start_node'], 'node2': row['end_node']}

    print("Loaded all edges")
    return nodes, edges

