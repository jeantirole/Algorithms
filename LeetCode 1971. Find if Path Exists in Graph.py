
# Pb : https://leetcode.com/problems/find-if-path-exists-in-graph/description/
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


# Sol : 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        paths = []
        visitied =[False for i in range(n)]

        import collections
        graph = collections.defaultdict(list)

        def make_graph():
            
            for edge in edges:
                s,t = edge
                graph[s].append(t)
                graph[t].append(s)

            for k,v in graph.items():
                graph[k] = list(set(v))
            
            #---------------------
        make_graph()

        #print("a")


        paths_ = []
        def dfs(start):

            if visitied[start] == True:
                return

            print(start)
            paths_.append(start)


            visitied[start] = True
            edges = graph[start]

            for edge in edges:
                dfs(edge)

        dfs(source)

        if destination in paths_:
            return True
        else:
            return False
        #print("b")

        
