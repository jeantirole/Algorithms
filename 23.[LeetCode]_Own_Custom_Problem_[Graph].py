#----------------------------------------- Problem

Custom problem set 

how to get all paths from graph? 
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

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
