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
