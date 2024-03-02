# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # array to tree
        # BFS => level order travels

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

        #--- print 
        # for i,re in enumerate(result):
        #     if i != 0:
        #         for r in re:
        #             print("rr", r.val)

        # implement reverse odd stage 
        for i,level in enumerate(result):
            if i % 2==0:
                pass
            elif i % 2 !=0:
                level.reverse()
        
        # #--- print 
        # for i,re in enumerate(result):
        #     if i != 0:
        #         for r in re:
        #             print("rr", r.val)
        
        
        def flatten_list(nested_list):
            flattened_list = []
            stack = list(nested_list)
            while stack:
                item = stack.pop(0)
                if isinstance(item, list):
                    stack.extend(item)
                else:
                    flattened_list.append(item)
            return flattened_list

        #----  
        a = flatten_list(result)
                
        array_s = [i.val for i in a]
        #print(array_s)

        # array to tree
        # array to tree
        # print(array_s)

        def array_to_tree(root_array):

            root =TreeNode(root_array[0])
            que = [root]

            cnt = 0
            while que:
                a = que.pop(0)

                cnt += 1
                if cnt < len(root_array):
                    if (root_array[cnt] != None):
                        a.left = TreeNode(root_array[cnt])
                        que.append(a.left)

                    cnt +=1
                    if ((root_array[cnt] != None)):
                        a.right = TreeNode(root_array[cnt])
                        que.append(a.right)
            return root 

        ss = array_to_tree(array_s)
 
        
        return ss

#---------------------------------------- User best 
https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/solutions/2590130/python3-bfs-and-dfs-with-line-by-line-comments
