#------------------------------------------------ Problem 

938. Range Sum of BST
Easy
Topics
Companies
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.




#------------------------------------------------ Solution 
# root = [10,5,15,3,7,None,18]
root = [10,5,15,3,7,13,18,1,None,6] 
tree = array_to_tree(root)
low = 6 
high = 10

#low= 7
#high= 15
sum = 0

#print(treenode_.val)
def dfs(tree_node):
  global sum 

  if tree_node.val != None:
    if low <= tree_node.val <= high :
      sum +=  tree_node.val
      print("added : ", tree_node.val)

  if tree_node == None:
    print("node None")
    return

  if tree_node.left:
    #print(tree_node.left.val)
    dfs(tree_node.left)
  
  if tree_node.right:
    #print(tree_node.right.val)
    dfs(tree_node.right)
  

#---

dfs(tree)

print(sum)
  
