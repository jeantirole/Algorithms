#-------------------- problem 
566. Reshape the Matrix
Solved
Easy
Topics
Companies
Hint
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.





#-------------------- solution
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        new_mat = []
        for row in mat:
            for num in row:
                flatten.append(num)
                
        if r * c != len(flatten):   # when given parameters is NOT possible and legal
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index * c : row_index * c + c])
            return new_mat
