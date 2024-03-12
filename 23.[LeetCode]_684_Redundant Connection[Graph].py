#------------------------------------ Problem
# Link : https://leetcode.com/problems/redundant-connection/description/

684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n 
where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.


#--------------------------------------- Solution 
https://leetcode.com/problems/redundant-connection/solutions/3876792/python3-dfs-with-clear-explanation/
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # variable to keep track of graph constructed so far
    graph_so_far = collections.defaultdict(lambda: [])
    
    # dfs function to check if path exists between nodes u and v
    def path_exists(u, v):
        # we reached to v from u
        if u == v:
            return True

        # mark u as visited
        visited.add(u)

        # iterate through all the neighbors of u and if they are not visited call dfs on them
        for neighbor in graph_so_far[u]:
            if neighbor not in visited:
                if path_exists(neighbor, v):
                    return True
                    
        return False

    # iterate through all the pairs of edges
    for u, v in edges:
        # we make a fresh visited because we call dfs for every pair of edges
        visited = set()
        # if path exists between u and v return that's the answer
        if path_exists(u,v):
            return [u,v]
        else:
            # if path does not exist we add edges to graph
            graph_so_far[u].append(v)
            graph_so_far[v].append(u)

    return None
