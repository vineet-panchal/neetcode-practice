# 102 - Binary Tree Level Order Traversal
# Leetcode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

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



# Solutions To The Problem:
from collections import deque

def levelOrder1(root: TreeNode):
  res = []

  q = deque()
  q.append(root)

  while q:
      qLen = len(q)
      level = []
      for i in range(qLen):
          node = q.popleft()
          if node:
              level.append(node.val)
              q.append(node.left)
              q.append(node.right)
      if level:
          res.append(level)

  return res



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def levelOrder(root: TreeNode):
  res = []
  def dfs(node, depth):
    if not node:
      return None
    if len(res) == depth: 
      res.append([])
    
    res[depth].append(node.val)
    dfs(node.left, depth + 1)
    dfs(node.right, depth + 1)

  dfs(root, 0)
  return res

if __name__ == "__main__":
  root = build_tree([1,2,3,4,5,6,7])
  root2 = build_tree([1])
  root3 = build_tree([])
  print("Test Case 1: ", [1, 2, 3, 4, 5, 6, 7])
  print("Expected Output: ", [[1], [2, 3], [4, 5, 6, 7]])
  print("Test Case 2: ", [1])
  print("Expected Output: ", [[1]])
  print("Test Case 3: ", [])
  print("Expected Output: ", [], "\n")
  
  levelTest1 = levelOrder(root)
  levelTest2 = levelOrder(root2)
  levelTest3 = levelOrder(root3)
  print("Depth First Search -> Test Case 1: ", levelTest1)
  print("Depth First Search -> Test Case 2: ", levelTest2)
  print("Depth First Search -> Test Case 3: ", levelTest3, "\n")
  
  level1Test1 = levelOrder1(root)
  level1Test2 = levelOrder1(root2)
  level1Test3 = levelOrder1(root3)
  print("Depth First Search -> Test Case 1: ", level1Test1)
  print("Depth First Search -> Test Case 2: ", level1Test2)
  print("Depth First Search -> Test Case 3: ", level1Test3, "\n")