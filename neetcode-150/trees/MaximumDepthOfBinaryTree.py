# 104 - Maximum Depth of Binary Tree
# Leetcode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
from collections import deque

# Breadth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepth2(root: TreeNode) -> int:
  q = deque()
  if root:
    q.append(root)

  level = 0
  while q:
    for i in range(len(q)):
      node = q.popleft()
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    level += 1
  return level



# Iterative Depth First Search Using Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepth1(root: TreeNode) -> int:
  stack = [[root, 1]] # create stack to go over the tree
  res = 0 # initialize result, the depth

  while stack: # while there are nodes
    node, depth = stack.pop() # unpack the tuple and get the node and depth

    if node: # if there is a node
      res = max(res, depth) # the result would be the max between the current result and the depth
      stack.append([node.left, depth + 1]) # put the left node and depth + 1 in the stack
      stack.append([node.right, depth + 1]) # put the right node adn depth + 1 in the stack
  return res # return the max depth



# Recursive Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepth(root: TreeNode) -> int:
  if not root: # if treee is empty
    return 0 # return 0, the tree has no depth
  
  count = 1 # else, the tree has at least depth of 1
  return count + max(maxDepth(root.left), maxDepth(root.right))
  # calculate the max depth by recursively checking the depth of left and right nodes
  # and only going with the max depth between the left and right

if __name__ == "__main__":
  print("Test Case 1: ", [3, 9, 20, None, None, 15, 7])
  print("Expected Output: ", 3)
  print("Test Case 2: ", [])
  print("Expected Output: ", 0, "\n")
  
  root = build_tree([3, 9, 20, None, None, 15, 7])
  root2 = build_tree([])
  
  depthRoot1 = maxDepth(root)
  print("Recursive Depth First Search -> Test Case 1: ", depthRoot1)
  depthRoot2 = maxDepth(root2)
  print("Recursive Depth First Search -> Test Case 2: ", depthRoot2, "\n")
  
  depth2Root1 = maxDepth1(root)
  print("Iterative Depth First Search -> Test Case 1: ", depth2Root1)
  depth2Root2 = maxDepth1(root2)
  print("Iterative Depth First Search -> Test Case 2: ", depth2Root2, "\n")
  
  depth3Root1 = maxDepth2(root)
  print("Breadth First Search -> Test Case 1: ", depth3Root1)
  depth3Root2 = maxDepth(root2)
  print("Breadth First Search -> Test Case 2: ", depth3Root2, "\n")