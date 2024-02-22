# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#----------------------------- Problem

103. Binary Tree Zigzag Level Order Traversal
Medium
Topics
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []





#----------------------------- Solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do bfs with switching between popleft and pop
        if not root:
            return 
        ans = []
        queue = deque([root])
        flip = 1
        while queue:
            n = len(queue)
            levelVal = []
            for _ in range(n):
                node = queue.popleft()
                levelVal.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(levelVal[::flip])
            flip *= -1
        return ans    
