# 572 - Subtree of Another Tree
# Leetcode Link: https://leetcode.com/problems/subtree-of-another-tree/

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
# Serialization and Pattern Matching
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
def serialize(root: TreeNode) -> str:
  if root == None:
    return "$#"

  return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))

def z_function(s: str) -> list:
  z = [0] * len(s)
  l, r, n = 0, 0, len(s)
  for i in range(1, n):
    if i <= r:
      z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
      z[i] += 1
    if i + z[i] - 1 > r:
      l, r = i, i + z[i] - 1
  return z

def isSubtree2(root: TreeNode, subRoot: TreeNode) -> bool:
  serialized_root = serialize(root)
  serialized_subRoot = serialize(subRoot)
  combined = serialized_subRoot + "|" + serialized_root

  z_values = z_function(combined)
  sub_len = len(serialized_subRoot)

  for i in range(sub_len + 1, len(combined)):
      if z_values[i] == sub_len:
          return True
  return False



# Depth First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
  if not subRoot: # if subroot is empty
    return True # then it is a subtree of root
  if not root: # if root tree empty 
    return False # then there cannot be a subroot
  if isSameTree(root, subRoot): # if the current node and the subtree is the same
    return True # then return true
  return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
  # recursively call and check with the left and right tree and compare it with subtree
  # the subtree can be either part of left or right tree

def isSameTree(p: TreeNode, q: TreeNode) -> bool: # helper function to check if two trees are the same
  if not p and not q:
    return True

  if p and q and p.val == q.val:
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
  return False

if __name__ == "__main__":
  root = build_tree([1, 2, 3, 4, 5])
  subroot = build_tree([2, 4, 5])
  root1 = build_tree([1, 2, 3, 4, 5, None, None, 6])
  subroot1 = build_tree([2, 4, 5])
  print("Test Case 1: root = ", [1, 2, 3, 4, 5], " subroot = ", [2, 4, 5])
  print("Expected Output: ", True)
  print("Test Case 2: root = ", [1, 2, 3, 4, 5, None, None, 6], " subroot = ", [2, 4, 5])
  print("Expected Output: ", False, "\n")
  
  subtreeTest1 = isSubtree(root, subroot)
  subtreeTest2 = isSubtree(root1, subroot1)
  print("Depth First Search -> Test Case 1: ", subtreeTest1)
  print("Depth First Search -> Test Case 2: ", subtreeTest2, "\n")
  
  subtree1Test1 = isSubtree2(root, subroot)
  subtree1Test2 = isSubtree2(root1, subroot1)
  print("Serialization and Pattern Matching -> Test Case 1: ", subtree1Test1)
  print("Serialization and Pattern Matching -> Test Case 2: ", subtree1Test2)