46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 


#---------------------
Solution
beats 99.61%

#---------------------

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.target_level = len(nums)-1
        self.target_list = [0 for _ in range(self.target_level + 1)]
        self.visited = [False for _ in range(len(nums))]
        self.result_ = []

        def dfs(node, level):
            val = nums[node]
            self.target_list[level] = val
            self.visited[node] = True

            if level == self.target_level:
                print(self.target_list)
                self.result_.append(self.target_list[:])  # Append a copy of target_list
                self.visited[node] = False  # Reset visited for backtracking
                return

            for i in range(len(nums)):
                if not self.visited[i]:
                    dfs(i, level + 1)
                    self.target_list[level + 1] = 0
                    self.visited[i] = False

        # Execute the DFS for each node
        for q in range(len(nums)):
            dfs(q, 0)
            # Reinitialize visited for the next iteration
            self.visited = [False for _ in range(len(nums))]

        return self.result_
