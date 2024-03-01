#--------------------------------- Problem 

1302. Deepest Leaves Sum
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 





#--------------------------------- Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if root.left == None and root.right == None:
            return root.val

        # level order travels 

        que = [root]

        cnt=0 

        tmp = []
        result = [root]
        while que:
            a = que.pop(0)
            
            if a.left and a.left != None:
                tmp.append(a.left)
            if a.right and a.right != None:
                tmp.append(a.right)

            if len(que) == 0 and len(tmp) !=0:
                result.append(tmp)
                que = tmp.copy()
                tmp = []

        return sum([i.val for i in result[-1]])


            
            
            
        

