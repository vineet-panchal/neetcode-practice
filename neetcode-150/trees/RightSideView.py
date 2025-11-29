# 199 - Binary Tree Right Side View
# Leetcode Link: https://leetcode.com/problems/binary-tree-right-side-view/

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

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
'''

# Solutions To The Problem:
from collections import deque

# Breadth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def rightSideView1(root: TreeNode):
  res = []
  q = deque([root])

  while q:
    rightSide = None
    qLen = len(q)

    for i in range(qLen):
      node = q.popleft()
      if node:
        rightSide = node
        q.append(node.left)
        q.append(node.right)
    if rightSide:
      res.append(rightSide.val)
  return res



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def rightSideView(root: TreeNode):
  res = []

  def dfs(node, depth):
    if not node:
      return None
    if depth == len(res):
      res.append(node.val)
    dfs(node.right, depth + 1)
    dfs(node.left, depth + 1)
  dfs(root, 0)
  return res

if __name__ == "__main__":
  root = build_tree([1, 2, 3, None, 5, None, 4])
  root1 = build_tree([1, 2, 3, 4, None, None, None, 5])
  root2 = build_tree([1, None, 3])
  root3 = build_tree([])
  print("Test Case 1: ", [1, 2, 3, None, 5, None, 4])
  print("Expected Output: ", [1, 3, 4])
  print("Test Case 2: ", [1, 2, 3, 4, None, None, None, 5])
  print("Expected Output: ", [1, 3, 4, 5])
  print("Test Case 3: ", [1, None, 3])
  print("Expected Output: ", [1, 3])
  print("Test Case 4: ", [])
  print("Expected Output: ", [], "\n")

  rightTest1 = rightSideView(root)
  rightTest2 = rightSideView(root1)
  rightTest3 = rightSideView(root2)
  rightTest4 = rightSideView(root3)
  print("Depth First Search -> Test Case 1: ", rightTest1)
  print("Depth First Search -> Test Case 2: ", rightTest2)
  print("Depth First Search -> Test Case 3: ", rightTest3)
  print("Depth First Search -> Test Case 4: ", rightTest4, "\n")

  right1Test1 = rightSideView1(root)
  right1Test2 = rightSideView1(root1)
  right1Test3 = rightSideView1(root2)
  right1Test4 = rightSideView1(root3)
  print("Breadth First Search -> Test Case 1: ", right1Test1)
  print("Breadth First Search -> Test Case 2: ", right1Test2)
  print("Breadth First Search -> Test Case 3: ", right1Test3)
  print("Breadth First Search -> Test Case 4: ", right1Test4, "\n")
