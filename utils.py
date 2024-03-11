# Array to TreeNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_tree(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    
    while queue:
        node = queue.pop(0)
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    
    return root