# 110 - Balanced Binary Tree
# Leetcode Link: https://leetcode.com/problems/balanced-binary-tree/

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
# Iterative Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isBalanced2(root):
  stack = []
  node = root
  last = None
  depths = {}

  while stack or node:
    if node:
      stack.append(node)
      node = node.left
    else:
      node = stack[-1]
      if not node.right or last == node.right:
        stack.pop()
        left = depths.get(node.left, 0)
        right = depths.get(node.right, 0)

        if abs(left - right) > 1:
          return False

        depths[node] = 1 + max(left, right)
        last = node
        node = None
      else:
        node = node.right

  return True



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isBalanced1(root: TreeNode) -> bool:
  def dfs(root):
    if not root:
      return [True, 0]

    left, right = dfs(root.left), dfs(root.right)
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    return [balanced, 1 + max(left[1], right[1])]

  return dfs(root)[0]


# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def isBalanced(root: TreeNode) -> bool:
  if not root: # if tree is empty
    return True # then return true

  left = depth(root.left) # calculate the depth of left subtree
  right = depth(root.right) # calculate the depth of right subtree
  if abs(left - right) > 1: # if the difference between the depths is more than 1
    return False # then tree is not balanced

  return isBalanced(root.left) and isBalanced(root.right)
  # recursively call isBalanced tree with both left and right subtree
  # it has to be true for both subtrees in order to be balanced

def depth(root: TreeNode) -> int: # helper function to calculate the depth of a tree
    if not root:
        return 0
    
    return 1 + max(depth(root.left), depth(root.right))

if __name__ == "__main__":
  root = build_tree([1, 2, 3, None, None, 4])
  root2 = build_tree([1, 2, 3, None, None, 4, None, 5])
  root3 = build_tree([])
  print("Test Case 1: ", [1, 2, 3, None, None, 4])
  print("Expected Output: ", True)
  print("Test Case 2: ", [1, 2, 3, None, None, 4, None])
  print("Expected Output: ", False)
  print("Test Case 3: ", [])
  print("Expected Output: ", True, "\n")
  
  balancedRoot1 = isBalanced(root)
  balancedRoot2 = isBalanced(root2)
  balancedRoot3 = isBalanced(root3)
  print("Brute Force -> Test Case 1: ", balancedRoot1)
  print("Brute Force -> Test Case 2: ", balancedRoot2)
  print("Brute Force -> Test Case 3: ", balancedRoot3, "\n")
  
  balanced1Root1 = isBalanced1(root)
  balanced1Root2 = isBalanced1(root2)
  balanced1Root3 = isBalanced1(root3)
  print("Brute Force -> Test Case 1: ", balanced1Root1)
  print("Brute Force -> Test Case 2: ", balanced1Root2)
  print("Brute Force -> Test Case 3: ", balanced1Root3, "\n") 
  
  balanced2Root1 = isBalanced2(root)
  balanced2Root2 = isBalanced2(root2)
  balanced2Root3 = isBalanced2(root3)
  print("Brute Force -> Test Case 1: ", balanced2Root1)
  print("Brute Force -> Test Case 2: ", balanced2Root2)
  print("Brute Force -> Test Case 3: ", balanced2Root3, "\n")