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

dfs(tree_root)
