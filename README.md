# Mad Map
Mad Map is a UW-Madison campus navigation system developed using a custom A* ([A Star](https://en.wikipedia.org/wiki/A*_search_algorithm)) pathfinding algorithm. Mad Map returns the quickest walkable route between any two points on campus.

<img src="https://github.com/EvanC8/Mad-Map/blob/main/CampusPlot.png?raw=true" height="300">

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#how-it-works">How it works</a>
      <ul>
        <li><a href="#Dataset">Dataset</a></li>
        <li><a href="#A*-Pathfinding">A* Pathfinding/a></li>
        <li><a href="#Visualization">Visualization</a></li>
      </ul>
    </li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

# Installation
* Clone the repo
   ```sh
   git clone https://github.com/EvanC8/Map-Map.git
   ```
# Usage
1. Download project
2. Ensure necessary dependencies are installed
3. Run `main.py` (Ensure that random <i>random_path</i> is set to <i>True</i>)
4. Watch Mad Map show you the quickest path being two random spots on campus!

# How it works
<img src="https://github.com/EvanC8/Mad-Map/blob/main/RouteExample1.png?raw=true" height="200">

### Dataset
The data on UW-Madison was retrieved using [OSMnx](https://osmnx.readthedocs.io/en/stable/), a python library for accessing street networks. Streets (edges) and intersections (nodes) were parsed and divided into seperate csv files for easy access and retrieval  of only the neccesarry details on roads. The data stored in each of these files is below:

| CSV File | Data |
|------------|-------|
| Streets (edges) | ID, Intersection 1 ID, Intersection 2 ID, Length (meters), Name, Oneway? |
| Intersections (nodes) | ID, Latitude, Longitude, Intersecting street IDs |

### A* Pathfinding
[A* pathfinding](https://en.wikipedia.org/wiki/A*_search_algorithm) efficiently finds the shortest path between two nodes by considering both the distance traveled so far (g(n)) and an estimated cost to the goal (h(n)). It prioritizes paths with the lowest total estimated cost (f(n) = g(n) + h(n)), allowing it to focus on the most promising routes that will reduce travel distance and time. This implementation of A* utilizes a min heap priority queue data structure to efficiently track and explore the most promising paths.

### Visualization
Once a route is found by the algorithm, it is plotted over a map of UW-Madison's campus using the library [NetworkX](https://networkx.org/).

# Next Steps
* Mad Map is currently being implemented as the foundation of an application being developed by a group of UW-Madison students. Stay tuned!

# License
Destributed under the MIT License. See `LICENSE.txt` for more information.

# Contact
Evan Cedeno - escedeno8@gmail.com

Project Link: [Mad Map](https://github.com/EvanC8/Mad-Map)
