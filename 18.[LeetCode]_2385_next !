#--------------------------------------------------- Problem 
Link : https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

2385. Amount of Time for Binary Tree to Be Infected

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 
Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.


#-------------------------------------------------- Solution 
# 1. solution class version (leetcode) 
# 2. debugging version 
# Comment
# approach => treenode_to_graphdict => bfs graph => level count from start node ! 


from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.graph_ = defaultdict(list)
        self.contam = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.tree_to_graph(root)

        visited = defaultdict(bool)
        for k in self.graph_:
            visited[k] = False 

        que_ = [start]
        stage_ = []

        while que_:
            n = que_.pop(0)
            visited[n] = True
            neigs = self.graph_[n]
        
            for adj in neigs:
                if not visited[adj]:
                    stage_.append(adj)

            if not que_:
                self.contam += 1 
                que_ = stage_
                stage_ = []

        return self.contam -1 

    def tree_to_graph(self, root):
        if root is None:
            return

        if root.left:
            self.graph_[root.val].append(root.left.val)
            self.graph_[root.left.val].append(root.val) 
            self.tree_to_graph(root.left)

        if root.right:
            self.graph_[root.val].append(root.right.val) 
            self.graph_[root.right.val].append(root.val)
            self.tree_to_graph(root.right)


#-- debug 
from collections import defaultdict

d_ = defaultdict(list)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        current_node = queue.pop(0)
        
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        
        i += 1
    
    return root

# Given list representation of the tree
nodes = [1, 5, 3, None, 4, 10, 6, 9, 2]

# Build the tree
tree_root = build_tree(nodes)


#--------------------------------------------------------------

# Print the tree structure
def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

print_tree(tree_root)


#--
    
print("done")


#------------------------------------------------------------------
def dfs(root):
  
  if root == None:
    return
  print(root.val)

  if root.left != None:
    #print(root.left.val)
    dfs(root.left)
  
  if root.right != None:
    #print(root.right.val)
    dfs(root.right)

#---
#dfs(tree_root)
    

#--------------------------------------------

graph_ = defaultdict(list)
def tree_to_graph(root):
    global graph_

    if root == None:
        return

    if root.left != None:
        
        graph_[root.val].append(root.left.val)
        graph_[root.left.val].append(root.val) 
        tree_to_graph(root.left)

    if root.right !=None:
       
        graph_[root.val].append(root.right.val) 
        graph_[root.right.val].append(root.val)
        tree_to_graph(root.right)

#---
tree_to_graph(tree_root)
print(graph_) 


#--------------------------------------------


visited = defaultdict()
for k,v in graph_.items():
    visited[k] = False 

start_node = 3
que_ = [start_node]

stage_= []

contam =0
while que_:
    n = que_.pop(0)
    # visit ! 
    visited[n] = True
    # nei
    neigs = graph_[n]
   
    for adj in neigs:
        if visited[adj] == False:
            stage_.append(adj)
            #que_.append(adj)
    
    #-- important 
    if len(que_) ==0:
        contam += 1 
        que_ = stage_
        stage_ = []


contam = contam -1 

print("# final contam : ",contam)
#------------------------------------------




