#--------------------------------------------------------
1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
Notice that you can return the vertices in any order.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].



#--------------------------------------------------------
# Sol 
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(g,c,vis,res):
            vis[c] = True
            for adj in g[c]:
                if not vis[adj]:
                    dfs(g,adj,vis,res)
                #adj can be visited by current vertex so we dont have to add adj in res
                elif adj in res:res.remove(adj)
        
        #Make a adjecency list
        g = collections.defaultdict(list)
        for e in edges:
            u,v = e
            g[u].append(v)
            
        
        res = set()
        vis = [False]*n
        for i in range(n):
            if not vis[i]:
                dfs(g,i,vis,res)
				#add vertex from which we start traversing
                res.add(i)
        return list(res)
