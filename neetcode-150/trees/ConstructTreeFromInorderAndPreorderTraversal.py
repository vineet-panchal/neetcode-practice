# 102 - Construct Binary Tree from Preorder and Inorder Traversal
# Leetcode Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
# Depth First Search 2
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def buildTree2(preorder, inorder) -> TreeNode:
  if not preorder or not inorder:
    return None

  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])
  root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
  root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
  return root



# Hash Map and Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def buildTree1(preorder, inorder) -> TreeNode:
  indices = {val: idx for idx, val in enumerate(inorder)}

  pre_idx = 0
  def dfs(l, r):
    if l > r:
      return None

    root_val = preorder[pre_idx]
    pre_idx += 1
    root = TreeNode(root_val)
    mid = indices[root_val]
    root.left = dfs(l, mid - 1)
    root.right = dfs(mid + 1, r)
    return root

  return dfs(0, len(inorder) - 1)



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def buildTree(preorder, inorder) -> TreeNode:
  preIdx = inIdx = 0
  def dfs(limit):
    nonlocal preIdx, inIdx
    if preIdx >= len(preorder):
      return None
    if inorder[inIdx] == limit:
      inIdx += 1
      return None

    root = TreeNode(preorder[preIdx])
    preIdx += 1
    root.left = dfs(root.val)
    root.right = dfs(limit)
    return root
  return dfs(float('inf'))

if __name__ == "__main__":
  preorder = build_tree([1, 2, 3, 4])
  inorder = build_tree([2, 1, 3, 4])
  preorder1 = build_tree([1])
  inorder1 = build_tree([1])
  print("Test Case 1: preorder = ", [1, 2, 3, 4], " inorder = ", [2, 1, 3, 4])
  print("Expected Output: ", [1, 2, 3, None, None, None, 4])
  print("Test Case 2: preorder = ", [1], " inorder = ", [1])
  print("Expected Output: ", [1], "\n")
  
  buildTest1 = buildTree(preorder, inorder)
  buildTest2 = buildTree(preorder1, inorder1)
  print("Depth First Search -> Test Case 1: ", level_order_traversal(buildTest1))
  print("Depth First Search -> Test Case 2: ", level_order_traversal(buildTest2), "\n")
  
  build1Test1 = buildTree1(preorder, inorder)
  build1Test2 = buildTree1(preorder1, inorder1)
  print("Hash Map and Depth First Search -> Test Case 1: ", level_order_traversal(build1Test1))
  print("Hash Map and Depth First Search -> Test Case 2: ", level_order_traversal(build1Test2), "\n")
  
  build2Test1 = buildTree2(preorder, inorder)
  build2Test2 = buildTree2(preorder1, inorder1)
  print("Depth First Search 2 -> Test Case 1: ", level_order_traversal(build2Test1))
  print("Depth First Search 2 -> Test Case 2: ", level_order_traversal(build2Test2), "\n")