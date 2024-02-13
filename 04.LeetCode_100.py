# Problem ------------------------------------------------------------------------

100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


# Solution ------------------------------------------------------------------------
(Mine)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_list= []
        q_list= []
        def dfs(node,signal):
            if node == None:
                #print("null")
                if signal =="p":
                    p_list.append("null")
                else:
                    q_list.append("null")
                return
            if signal =="p":
                    p_list.append(node.val)
            else:
                    q_list.append(node.val)
            dfs(node.left,signal)
            dfs(node.right,signal)
            
        dfs(p,"p")
        # print("#---")
        dfs(q,"q")
        return p_list == q_list
            
             
         
        
