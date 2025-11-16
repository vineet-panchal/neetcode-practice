# 1448 - Count Good Nodes In Binary Tree
# Leetcode Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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
def goodNodes1(root: TreeNode) -> int:
  res = 0
  q = deque()
  q.append((root,-float('inf')))

  while q:
    node,maxval = q.popleft()
    if node.val >= maxval:
      res += 1
    if node.left:
      q.append((node.left,max(maxval,node.val)))
    if node.right:
      q.append((node.right,max(maxval,node.val)))

  return res

# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def goodNodes(root: TreeNode) -> int:
  def dfs(node, maxVal):
    if not node:
      return 0
    
    res = 1 if node.val >= maxVal else 0
    maxVal = max(maxVal, node.val)
    res += dfs(node.left, maxVal)
    res += dfs(node.right, maxVal)
    return res
  return dfs(root, root.val)

if __name__ == "__main__":
  root = build_tree([3, 1, 4, 3, None, 1, 5])
  root1 = build_tree([3, 3, None, 4, 2])
  root2 = build_tree([1])
  print("Test Case 1: ", root)
  print("Expected Output: ", 4)
  print("Test Case 2: ", root1)
  print("Expected Output: ", 3)
  print("Test Case 3: ", root2)
  print("Expected Output: ", 1, "\n")
  
  goodTest1 = goodNodes(root)
  goodTest2 = goodNodes(root1)
  goodTest3 = goodNodes(root2)
  print("Depth First Search -> Test Case 1: ", goodTest1)
  print("Depth First Search -> Test Case 2: ", goodTest2)
  print("Depth First Search -> Test Case 3: ", goodTest3, "\n")
  
  good1Test1 = goodNodes1(root)
  good1Test2 = goodNodes1(root1)
  good1Test3 = goodNodes1(root2)
  print("Breadth First Search -> Test Case 1: ", good1Test1)
  print("Breadth First Search -> Test Case 2: ", good1Test2)
  print("Breadth First Search -> Test Case 3: ", good1Test3, "\n")