#----------------------------- Problem
1261. Find Elements in a Contaminated Binary Tree
Medium
Topics
Companies
Hint
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

  
#-------------------------------- Solution 


in_ = [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
#in_ = [[[-1,None,-1]],[1],[2]]
   
arrray_tree = in_[0][0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# array to tree 

root = TreeNode(arrray_tree[0])
que= [root]

cnt= 0 
print(cnt)
while que:
  
  a = que.pop(0)
  
  cnt +=1
  print(cnt)
  if cnt < len(arrray_tree):
    a.left = TreeNode(arrray_tree[cnt])
    que.append(a.left)  
  cnt +=1
  print(cnt)
  if cnt < len(arrray_tree):
    a.right = TreeNode(arrray_tree[cnt])
    que.append(a.right)

#---
# def ! tree recover ! 

# iteration & function 

#----
que_two = [0]
#---

que=[root]

cnt= 0
print(cnt)
while que:
    
  b = que.pop(0)
  
  #print("b.left.val : ",b.left.val)
  if (cnt < len(arrray_tree)) :
    
    cnt +=1 
    print(cnt)

    if cnt == len(arrray_tree):
     break

    if b.left.val != None:
      b.left.val = cnt
      que_two.append(cnt)
    else:
      pass
    que.append(b.left)
    
    cnt +=1
    print(cnt) 

    if b.right.val != None:
      b.right.val = cnt
      que_two.append(cnt)
    else:
      pass
    
    que.append(b.right)

#--- 
root.val = 0


#---
for i in range(1,len(in_)):
  
  if in_[i][0] in que_two:
    print("True")
  else:
    print("False")

que_two
