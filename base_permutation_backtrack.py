
from itertools import permutations, combinations
data = ["a","b","c"]
result = list(permutations(data,2))
print("answer : ",result)


data = ["a","b","c"]
target_level = 1 
target_list = [0 for i in range(target_level+1)]
visited = [False for i in range(len(data))]

def dfs(node,visited,level):
    

    val = data[node]
    target_list[level] = val
    visited[node] = True

    if level == target_level:
        print(target_list)
        return
    

    for i in range(len(data)):
        if visited[i] != True: 
            dfs(i,visited,level+1)
            target_list[level+1] = 0
            visited[i] = False

#---- exec
for q in range(len(data)):
    dfs(q,visited,0)
    #-- init 
    visited = [False for i in range(len(data))]
            
    
    
