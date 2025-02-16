import osmnx as ox
import geopandas as gpd

# Get the street network for UW-Madison - walkable paths
G = ox.graph_from_place("University of Wisconsin-Madison, Wisconsin, USA", network_type="walk")

# Convert the graph to a GeoDataFrame
gdf_edges = ox.graph_to_gdfs(G, nodes=False, edges=True)

# Save as Shapefile
gdf_edges.to_file("uw_madison_streets.shp")

# Save as GeoJSON #Extra
gdf_edges.to_file("uw_madison_streets.geojson", driver="GeoJSON")

# Plot street network
ox.plot_graph(G)
