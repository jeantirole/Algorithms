#----------------------------- Problem
# Link : https://leetcode.com/problems/max-area-of-island/description/

# 695. Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
 
# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0




#---------------------------- Solution
# Simple DFS !! 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        # matrix = [[1,1,0,0],
        #   [1,1,1,0],
        #   [1,0,0,0],
        #   [0,0,0,0]]

        matrix = grid
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
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    local_sum = 0
                    max_sum = max(max_sum, dfs(i, j, local_sum))

        print("Max Sum:", max_sum)

        return max_sum

# Using Stack iteration ,, !! more efficient 

# DFS using stack 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r,c):
            if (
                r<0 or c<0
                or r==len(grid) or c==len(grid[0])
                or grid[r][c] != 1
            ):
                return 0

            grid[r][c] = 'v'

            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area,dfs(r,c))

        return max_area



# Sample 

matrix = [[1,1,0,0],
          [1,1,1,0],
          [1,0,0,0],
          [0,0,0,0]]

def dfs(x, y):
    stack = [(x, y)]
    local_sum = 0

    while stack:
        x, y = stack.pop()
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 1:
            local_sum += 1
            matrix[x][y] = 0
            stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    return local_sum

max_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            local_sum = dfs(i, j)
            max_sum = max(max_sum, local_sum)

print("Max Sum:", max_sum)
