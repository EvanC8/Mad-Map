import osmnx as ox
import pandas as pd

# Load only **walkable** paths for UW-Madison
G = ox.graph_from_place("University of Wisconsin-Madison, Wisconsin, USA", network_type="walk")

# Convert graph to GeoDataFrames
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

# ---- CREATE EDGES DATAFRAME ----

# Create a unique ID for each edge
gdf_edges = gdf_edges.reset_index()  # Ensure edges have an index
gdf_edges["edge_id"] = gdf_edges.index  # Use index as a unique ID

# Keep only relevant columns (no "sidewalk" anymore)
columns_to_keep = ["edge_id", "u", "v", "length", "name", "oneway"]
edges_df = gdf_edges[columns_to_keep].copy()

# Rename columns for clarity
edges_df.rename(columns={"u": "start_node", "v": "end_node"}, inplace=True)

# Save edges CSV
edges_df.to_csv("uw_madison_edges.csv", index=False)

# ---- CREATE NODES DATAFRAME ----

# Prepare node data with neighboring edges
nodes_data = []
for node_id, row in gdf_nodes.iterrows():
    # Find all edges connected to this node
    neighbor_edges = gdf_edges[(gdf_edges["u"] == node_id) | (gdf_edges["v"] == node_id)]["edge_id"].tolist()

    nodes_data.append({
        "node_id": node_id,
        "lat": row["y"],
        "lon": row["x"],
        "neighbor_edges": ";".join(map(str, neighbor_edges))  # Store as a semicolon-separated string
    })

# Convert to a DataFrame
nodes_df = pd.DataFrame(nodes_data)

# Save nodes CSV
nodes_df.to_csv("uw_madison_nodes.csv", index=False)

print("Walkable nodes and edges saved to 'uw_madison_nodes.csv' and 'uw_madison_edges.csv'.")

