from AStar import AStar
from parse_street_data import parse_street_data
import random

# Initialize pathfinder
astar = AStar()

# If TRUE - Generates path between two randomly selected nodes (intersections)
# If FALSE - Generates path between two known node (intersection) IDs
random_path = True

nodes, edges = parse_street_data()

if random_path:
    astar.find_path(random.choice(list(nodes.keys())), random.choice(list(nodes.keys())))
else:
    astar.find_path(10748463808, 5445903897)