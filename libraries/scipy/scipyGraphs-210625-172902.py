##############################################################

# SciPy Graphs
# Graphs are an essential data structure.
# SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

# Adjacency Matrix
# Adjacency matrix is a nxn matrix where n is the number of elements in a graph.
# And the values represents the connection between the elements.

##############################################################

# Example: graph
# A & B are connected with weight 1.
# A & C are connected with weight 2.
# C & B is not connected.
# The Adjency Matrix would look like this:
#       A B C
#    A:[0 1 2]  
#    B:[1 0 0]
#    C:[2 0 0]

##############################################################

# Connected Components
# Find all of the connected components with the connected_components() method.

# import numpy as np
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse import csr_matrix
# arr = np.array([
#   [0, 1, 2],
#   [1, 0, 0],
#   [2, 0, 0]
# ])
# arr = np.array([
#   [0, 1, 2,0,0],
#   [1, 0, 0,0,0],
#   [2, 0, 0,0,0],
#   [0, 0, 0,0,0],
#   [3, 0, 0,0,0],
# ])
# arr = np.array([[0, 1, 1, 0, 0, 0, 0],
#        [1, 0, 1, 0, 0, 0, 0],
#        [1, 1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0, 1],
#        [0, 0, 0, 1, 0, 1, 0],
#        [0, 0, 0, 0, 1, 0, 1],
#        [0, 0, 0, 1, 0, 1, 0]])
# newarr = csr_matrix(arr)
# print(connected_components(newarr))

##############################################################

# Dijkstra
# Use the dijkstra method to find the shortest path in a graph from one element to another.
# It takes following arguments:
# 1.	return_predecessors: boolean.
# 2.	indices: index of the element to return all paths from that element only.
# 3.	limit: max weight of path.


# Find the shortest path from element 1 to 2:
# import numpy as np
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse import csr_matrix
# arr = np.array([
#   [0, 1, 2],
#   [1, 0, 0],
#   [2, 0, 0] ])
# newarr = csr_matrix(arr)
# print(dijkstra(newarr, return_predecessors=True, indices=0))

##############################################################

# Floyd Warshall
# Use the floyd_warshall() method to find shortest path between all pairs of elements.

# Find the shortest path between all pairs of elements:
# import numpy as np
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse import csr_matrix
# arr = np.array([
#   [0, 1, 2],
#   [1, 0, 0],
#   [2, 0, 0]
# ])
# newarr = csr_matrix(arr)
# print(floyd_warshall(newarr, return_predecessors=True))

##############################################################

# Bellman Ford
# The bellman_ford() method can also find the shortest path between all pairs of elements, 
# but this method can handle negative weights as well.

# Find shortest path from element 1 to 2 with given graph with a negative weight:
# import numpy as np
# from scipy.sparse.csgraph import bellman_ford
# from scipy.sparse import csr_matrix
# arr = np.array([
#   [0, -1, 2],
#   [1, 0, 0],
#   [2, 0, 0]
# ])
# newarr = csr_matrix(arr)
# print(bellman_ford(newarr, return_predecessors=True, indices=0))

##############################################################
##############################################################
