#----------------------------------------- Geeks
# Python program to print all paths from a source to destination.
# Link : https://www.geeksforgeeks.org/find-paths-given-source-destination/
from collections import defaultdict

# This class represents a directed graph 
# using adjacency list representation
class Graph:

	def __init__(self, vertices):
		# No. of vertices
		self.V = vertices 
		
		# default dictionary to store graph
		self.graph = defaultdict(list) 

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	'''A recursive function to print all paths from 'u' to 'd'.
	visited[] keeps track of vertices in current path.
	path[] stores actual vertices and path_index is current
	index in path[]'''
	def printAllPathsUtil(self, u, d, visited, path):

		# Mark the current node as visited and store in path
		visited[u]= True
		path.append(u)

		# If current vertex is same as destination, then print
		# current path[]
		if u == d:
			print (path)
		else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
			for i in self.graph[u]:
				if visited[i]== False:
					self.printAllPathsUtil(i, d, visited, path)
					
		# Remove current vertex from path[] and mark it as unvisited
		path.pop()
		visited[u]= False


	# Prints all paths from 's' to 'd'
	def printAllPaths(self, s, d):

		# Mark all the vertices as not visited
		visited =[False]*(self.V)

		# Create an array to store paths
		path = []

		# Call the recursive helper function to print all paths
		self.printAllPathsUtil(s, d, visited, path)



# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav


#----------------------------------------- Problem

Custom problem set 

how to get all paths from graph? from source to target
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

from 1 to 4

#------------------------------------------ Guide
# Method to print all paths between two nodes using DFS approach.
# Graph is represented as Adjacency List.
# Total number of nodes = n.
# So, n = adjacencyList.size()// Nodes are marked from 0 to (n - 1)
# Adjacency List will contain entries for all nodes, if a node
# has no adjacent node, then the adjacency list will contain an empty list
def printAllPaths(self, adjacencyList, source, destination):
    beingVisited = [False for _ in range(len(adjacencyList))]
    currentPath = []
    currentPath.append(source)
    self._dfs(adjacencyList, source, destination, beingVisited, currentPath)

def _dfs(self, graph, source, destination, beingVisited, currentPath):
    if source == destination:
        printPath(currentPath)  # TODO: implement method to print the path
        return
    beingVisited[source] = True  # to avoid cycle
    for i in graph[source]:  # loop over all adjacent nodes
        if not beingVisited[i]:
            currentPath.append(i)
            self._dfs(graph, i, destination, beingVisited, currentPath)
            currentPath.pop(i)
    beingVisited[source] = False 



#----------------------------------------- Solution

def dfs_all_paths(graph, start, visited=None, path=None, all_paths=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_all_paths(graph, neighbor, visited, path, all_paths)

    all_paths.append(path.copy())

    path.pop()
    visited.remove(start)

    return all_paths

# Example usage
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
start_node = 0
all_paths = dfs_all_paths(graph, start_node)

print("All paths from node", start_node, ":")
for path in all_paths:
    print(path)


#------------------------------------- 
