#--- Pb 
807. Max Increase to Keep City Skyline

There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

#---
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        import numpy as np 
        # grid = [[3,0,8,4],
        #         [2,4,5,7],
        #         [9,2,6,3],
        #         [0,3,1,0]]
        grid = np.asarray(grid)
        
        sum = 0
        shape_ = grid.shape
        for i in range(shape_[0]):
            for j in range(shape_[1]):        
                ele = grid[i][j]
                ele_min = min( max(grid[i,:]), max(grid[:,j]))
                
                sum += abs(ele_min - ele)
                grid[i][j] = ele_min
        return sum

#--- best solution beat 100% 
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Find the maximum elements in each row and column
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]  # Efficient zip for columns

        # Calculate the total increase while maintaining the skyline
        total_increase = 0
        for r in range(n):
            for c in range(n):
                total_increase += min(row_max[r], col_max[c]) - grid[r][c]

        return total_increase


