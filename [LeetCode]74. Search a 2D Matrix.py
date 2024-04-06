Pb : https://leetcode.com/problems/search-a-2d-matrix/description/

74. Search a 2D Matrix

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false



Sol : https://leetcode.com/problems/search-a-2d-matrix/solutions/1895915/python-3-short-and-readable-solutions/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        def get(idx: int) -> int:
            r, c = divmod(idx, n)
            return matrix[r][c]
        return get(bisect_left(range(len(matrix)*n-1), target, key=get)) == target


