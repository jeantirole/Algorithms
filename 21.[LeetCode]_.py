from utils import array_to_tree

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]


rows = len(grid)
cols = len(grid[0])

max_count = 0 
for r in range(rows):
    for c in range(cols):
        visit = grid[r][c]
        if visit == 1:
            # dfs
            ## dfs makes every cells in the grid 0 and count numbers of 1
            pass
        else:
            pass            
             
#-------------------------
# matrix = grid.copy()
matrix = [[1,1,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [0,0,0,0]]
#------------------------- 
max_sum = 0


def dfs(x,y,local_sum):
    
    global max_sum
    global matrix
 
    if matrix[x][y] == None:
        return local_sum
    if matrix[x][y] ==0:
        return local_sum
    elif matrix[x][y] ==1:
        matrix[x][y] = 0 
        #max_sum += 1
        local_sum += 1
        
    #------     
    # to the right 
    if matrix[x+1][y] == 1 :
        dfs(x+1,y,local_sum )
    
    # to the left 
    if matrix[x-1][y] == 1:
        dfs(x-1,y,local_sum )
    
    # to the up
    if matrix[x][y+1] == 1:
        dfs(x,y+1,local_sum )
    
    # to the down
    if matrix[x][y-1] == 1:
        dfs(x,y-1,local_sum )
    
    return local_sum

#--------------------------    
a = dfs(0,0,0)

print("local sum : ", a )
print(matrix)
print("done")



        

#     #----     
#     # to the right 
#     right_x = position[0] + 1
#     right_y = position[1]
#     right_pos = [right_x,right_y ]
#     if matrix[right_pos] != 0 or None:
#         dfs(right_pos)
    
#     # to the left 
#     left_x = position[0] - 1 
#     left_y = position[1]
#     left_pos = [left_x,left_y ]
#     if matrix[left_pos] != 0 or None:
#         dfs(left_pos)
    
#     # to the up
#     up_x = position[0]  
#     up_y = position[1] + 1 
#     up_pos = [up_x,up_y]
#     if matrix[up_pos] != 0 or None:
#         dfs(up_pos)
    
#     # to the down
#     down_x = position[0]  
#     down_y = position[1] - 1
#     down_pos = [down_x, down_y]
#     if matrix[down_pos] != 0 or None:
#         dfs(down_pos)
    
# #--------------------------    
# dfs([0,0])