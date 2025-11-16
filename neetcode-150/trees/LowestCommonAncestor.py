# 235 - Lowest Common Ancestor of a Binary Search Tree
# Leetcode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
# Recursion
# Space Complexity: O(n)
# Time Complexity: O(n)
def lowestCommonAncestor1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
  if not root or not p or not q:
    return None
  if (max(p.val, q.val) < root.val):
    return lowestCommonAncestor1(root.left, p, q)
  elif (min(p.val, q.val) > root.val):
    return lowestCommonAncestor1(root.right, p, q)
  else:
    return root



# Iteration
# Time Complexity: O(n)
# Space Complexity: O(1)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
  cur = root # set current ancestor node to be the root
  while cur: # while our ancestor node isn't null
    if p.val > cur.val and q.val > cur.val:
    # if both p and q is bigger than current ancestor
      cur = cur.right # then our ancestor would be on the right
    if p.val < cur.val and q.val < cur.val:
    # if both p and q is smaller than current ancestor
      cur = cur.left # then our ancestor would be on the left
    else: # else if both p and q are on opposite sides
      return cur # we have found our ancestor

if __name__ == "__main__":
  root = build_tree([5, 3, 8, 1, 4, 7, 9, None, 2])
  p = build_tree([3])
  q = build_tree([8])
  p1 = build_tree([3])
  q1 = build_tree([4])
  print("Test Case 1: root = ", [5, 3, 8, 1, 4, 7, 9, None, 2], " p = ", 3, " q = ", 8)
  print("Expected Output: ", 5)
  print("Test Case 2: root = ", [5, 3, 8, 1, 4, 7, 9, None, 2], " p = ", 3, " q = ", 4)
  print("Expected Output: ", 3, "\n")
  
  ancestorTest1 = lowestCommonAncestor(root, p, q)
  ancestorTest2 = lowestCommonAncestor(root, p1, q1)
  print("Iteration -> Test Case 1: ", level_order_traversal(ancestorTest1))
  print("Iteration -> Test Case 2: ", level_order_traversal(ancestorTest2), "\n")
  
  ancestor1Test1 = lowestCommonAncestor1(root, p, q)
  ancestor1Test2 = lowestCommonAncestor1(root, p1, q1)
  print("Iteration -> Test Case 1: ", level_order_traversal(ancestor1Test1))
  print("Iteration -> Test Case 2: ", level_order_traversal(ancestor1Test2), "\n")