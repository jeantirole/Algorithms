


matrix = [[1,1,0,0],
    [1,1,1,0],
    [1,0,0,1],
    [0,0,0,1]]

matrix 

#---------------------------------------------
def dfs(x, y, local_sum):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return local_sum
    if matrix[x][y] != 1:
        return local_sum

    local_sum += 1
    matrix[x][y] = 0

    local_sum = dfs(x+1, y, local_sum)
    local_sum = dfs(x-1, y, local_sum)
    local_sum = dfs(x, y+1, local_sum)
    local_sum = dfs(x, y-1, local_sum)

    return local_sum

max_sum = 0


#--- max sum to other page ! 
import numpy as np 
np_matrix = np.asanyarray(matrix)
rr= np.where(np_matrix == 1)

for q,k in zip(rr[0],rr[1]):
    print(q,k)
    local_sum = 0
    max_sum = max(max_sum, dfs(q, k, local_sum))



# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == 1:
#             local_sum = 0
#             max_sum = max(max_sum, dfs(i, j, local_sum))

print("Max Sum:", max_sum)

#return max_sum
