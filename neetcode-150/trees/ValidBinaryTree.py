# 98 - Valid Binary Tree
# Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/

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

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
left_check = staticmethod(lambda val, limit: val < limit)
right_check = staticmethod(lambda val, limit: val > limit)

def isValidBST2(root: TreeNode) -> bool:
  if not root:
    return True

  if (not isValid(root.left, root.val, left_check) or not isValid(root.right, root.val, right_check)):
    return False

  return isValidBST2(root.left) and isValidBST2(root.right)

def isValid(root: TreeNode, limit: int, check) -> bool:
  if not root:
    return True
  if not check(root.val, limit):
    return False
  return (isValid(root.left, limit, check) and isValid(root.right, limit, check))



# Breadth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isValidBST1(root: TreeNode) -> bool:
  if not root:
    return True

  q = deque([(root, float("-inf"), float("inf"))])

  while q:
    node, left, right = q.popleft()
    if not (left < node.val < right):
      return False
    if node.left:
      q.append((node.left, left, node.val))
    if node.right:
      q.append((node.right, node.val, right))

  return True



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isValidBST(root: TreeNode) -> bool:
  def valid(node, left, right):
    if not node:
      return True
    if not (left < node.val < right):
      return False
    return valid(node.left, left, node.val) and valid(node.right, node.val, right)
  return valid(root, float("-inf"), float("inf"))

if __name__ == "__main__":
  root = build_tree([2, 1, 3])
  root1 = build_tree([1, 2, 3])
  print("Test Case 1: ", [2, 1, 3])
  print("Expected Output: ", True)
  print("Test Case 2: ", [1, 2, 3])
  print("Expected Output: ", False, "\n")
  
  validTest1 = isValidBST(root)
  validTest2 = isValidBST(root1)
  print("Depth First Search -> Test Case 1: ", validTest1)
  print("Depth First Search -> Test Case 2: ", validTest2, "\n")
  
  valid1Test1 = isValidBST1(root)
  valid1Test2 = isValidBST1(root1)
  print("Breadth First Search -> Test Case 1: ", valid1Test1)
  print("Breadth First Search -> Test Case 2: ", valid1Test2, "\n")
  
  valid2Test1 = isValidBST2(root)
  valid2Test2 = isValidBST2(root1)
  print("Brute Force -> Test Case 1: ", valid2Test1)
  print("Brute Force -> Test Case 2: ", valid2Test2, "\n")