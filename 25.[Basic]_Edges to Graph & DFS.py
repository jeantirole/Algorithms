n = 6 

edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

visited = [False for i in range(n)]

from collections import defaultdict

graph = defaultdict(list)
for k in range(0,n):
    graph[k] =[] 

# make graph
for edge in edges:
    s = edge[0]
    d = edge[1]
        
    graph[s].append(d)


print(graph)


def dfs(node,path):
    
    path.append(node)
    
    if graph[node].__len__() ==0:
        print("path : ", path)
        path.pop()
        return
    
    neis = graph[node]
    for nei in neis:
        dfs(nei,path)
    
    path.pop()
    
    
#-------
start= 0
path = []

dfs(start, path)
    
    
