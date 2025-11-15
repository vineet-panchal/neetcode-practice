# 543 - Diameter Of Binary Tree
# Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def build_tree(values):
  if not values:
    return None
  root = TreeNode(values[0])
  queue = [root]
  i = 1
  while i < len(values):
    node = queue.pop(0)
    if values[i] is not None:
      node.left = TreeNode(values[i])
      queue.append(node.left)
    i += 1
    if i < len(values) and values[i] is not None:
      node.right = TreeNode(values[i])
      queue.append(node.right)
    i += 1
  return root

def level_order_traversal(root):
  if not root:
    return []
  result = []
  queue = [root]
  while queue:
    node = queue.pop(0)
    result.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return result



# Solutions To The Problem:

def diameterOfBinaryTree3(root):
  """
  :type root: Optional[TreeNode]
  :rtype: int
  """
  # Define a recursive function to calculate the diameter
  def diameter(node, res):
    # Base case: if the node is None, return 0
    if not node:
        return 0
    
    # Recursively calculate the diameter of left and right subtrees
    left = diameter(node.left, res)
    right = diameter(node.right, res)

    # Update the maximum diameter encountered so far
    res[0] = max(res[0], left + right)
    
    # Return the depth of the current node
    return max(left, right) + 1
  
  # Initialize a list to hold the maximum diameter encountered
  res = [0]
  # Call the diameter function starting from the root
  diameter(root, res)
  # Return the maximum diameter encountered
  return res[0]


# Iterative Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def diameterOfBinaryTree2(root: TreeNode) -> int:
  stack = [root]
  mp = {None: (0, 0)}

  while stack:
    node = stack[-1]

    if node.left and node.left not in mp:
      stack.append(node.left)
    elif node.right and node.right not in mp:
      stack.append(node.right)
    else:
      node = stack.pop()

      leftHeight, leftDiameter = mp[node.left]
      rightHeight, rightDiameter = mp[node.right]

      mp[node] = (1 + max(leftHeight, rightHeight),
                  max(leftHeight + rightHeight, leftDiameter, rightDiameter))

  return mp[root][1]



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def diameterOfBinaryTree1(root: TreeNode) -> int:
  res = 0 # initialize result

  def dfs(root): # dfs function
    nonlocal res # initialize a nonlocal resulting variable

    if not root: # if tree is empty
      return 0 # the diameter would be 0
    left = dfs(root.left) # get the left node
    right = dfs(root.right) # get the right node
    res = max(res, left + right) # 

    return 1 + max(left, right)

  dfs(root)
  return res



# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def diameterOfBinaryTree(root: TreeNode) -> int:
  if not root: 
    return 0
        
  leftHeight = maxHeight(root.left)
  rightHeight = maxHeight(root.right)
  diameter = leftHeight + rightHeight
  sub = max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))
  return max(diameter, sub)

def maxHeight(root: TreeNode) -> int:
  if not root:
    return 0
        
  return 1 + max(maxHeight(root.left), maxHeight(root.right))

if __name__ == "__main__":
  root = build_tree([1, None, 2, 3, 4, 5])
  root2 = build_tree([1, 2, 3])
  root3 = build_tree([1, 2])
  print("Test Case 1: " [1, None, 2, 3, 4, 5])
  print("Expected Output: ", 3)
  print("Test Case 2: ", [1, 2, 3])
  print("Expected Output: ", 2)
  print("Test Case 3: ", [1, 2])
  print("Expected Output: ", 1, "\n")
  
  diameterRoot = diameterOfBinaryTree(root)
  diameterRoot2 = diameterOfBinaryTree(root2)
  diameterRoot3 = diameterOfBinaryTree(root3)
  print("Brute Force -> Test Case 1: ", level_order_traversal(diameterRoot))
  print("Brute Force -> Test Case 2: ", level_order_traversal(diameterRoot2))
  print("Brute Force -> Test Case 3: ", level_order_traversal(diameterRoot3, "\n"))
  
  diameter1Root = diameterOfBinaryTree1(root)
  diameter1Root2 = diameterOfBinaryTree1(root2)
  diameter1Root3 = diameterOfBinaryTree1(root3)
  print("Depth First Search -> Test Case 1: ", level_order_traversal(diameter1Root))
  print("Depth First Search -> Test Case 1: ", level_order_traversal(diameter1Root2))
  print("Depth First Search -> Test Case 1: ", level_order_traversal(diameter1Root3), "\n")
  
  diameter2Root = diameterOfBinaryTree2(root)
  diameter2Root2 = diameterOfBinaryTree2(root2)
  diameter2Root3 = diameterOfBinaryTree2(root3)
  print("Iterative Depth First Search -> Test Case 1: ", level_order_traversal(diameter2Root))
  print("Iterative Depth First Search -> Test Case 1: ", level_order_traversal(diameter2Root2))
  print("Iterative Depth First Search -> Test Case 1: ", level_order_traversal(diameter2Root3), "\n")
  
  diameter3Root = diameterOfBinaryTree2(root)
  diameter3Root2 = diameterOfBinaryTree2(root2)
  diameter3Root3 = diameterOfBinaryTree2(root3)
  print("Brute Force 2 -> Test Case 1: ", level_order_traversal(diameter3Root))
  print("Brute Force 2 -> Test Case 1: ", level_order_traversal(diameter3Root2))
  print("Brute Force 2 -> Test Case 1: ", level_order_traversal(diameter3Root3))