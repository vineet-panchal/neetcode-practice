# 230 - Kth Smallest Integer in a BST
# Leetcode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
# Morris Traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
def kthSmallest4(root: TreeNode, k: int) -> int:
  curr = root

  while curr:
    if not curr.left:
      k -= 1
      if k == 0:
        return curr.val
      curr = curr.right
    else:
      pred = curr.left
      while pred.right and pred.right != curr:
        pred = pred.right

      if not pred.right:
        pred.right = curr
        curr = curr.left
      else:
        pred.right = None
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
  return -1


# Iterative Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def kthSmallest3(root: TreeNode, k: int) -> int:
  stack = []
  curr = root
  while stack or curr:
    while curr:
      stack.append(curr)
      curr = curr.left
    curr = stack.pop()
    k -= 1
    if k == 0:
      return curr.val
    curr = curr.right

# Recursive Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def kthSmallest2(root: TreeNode, k: int) -> int:
  cnt = k
  res = root.val
  def dfs(node):
    nonlocal cnt, res
    if not node:
      return 
    dfs(node.left)
    cnt -= 1
    if cnt == 0:
      res = node.val
      return
    dfs(node.right)
  dfs(root)
  return res



# In-Order Traversal
# Time Complexity: O(n)
# Space Complexity: O(n)
def kthSmallest1(root: TreeNode, k: int) -> int:
  arr = []
  def dfs(node):
    if not node:
      return
    dfs(node.left)
    arr.append(node.val)
    dfs(node.right)
  dfs(root)
  return arr[k - 1]


# Brute Force
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def kthSmallest(root: TreeNode, k: int) -> int:
  arr = []
  def dfs(node):
    if not node:
      return
    arr.append(node.val)
    dfs(node.left)
    dfs(node.right)
  dfs(root)
  arr.sort()
  return arr[k - 1]

if __name__ == "__main__":
  root = build_tree([3, 1, 4, None, 2])
  k = 1
  root1 = build_tree([5, 3, 6, 2, None, None, 1])
  k1 = 3
  root2 = build_tree([2, 1, 3])
  k2 = 1
  root3 = build_tree([4, 3, 5, 2, None])
  k3 = 4
  print("Test Case 1: root = ", root, " k = ", k)
  print("Expected Output: ", 1)
  print("Test Case 2: root = ", root1, " k = ", k1)
  print("Expected Output: ", 3)
  print("Test Case 3: root = ", root2, " k = ", k2)
  print("Expected Output: ", 1)
  print("Test Case 4: root = ", root3, " k = ", k3)
  print("Expected Output: ", 5, "\n")
  
  smallestTest1 = kthSmallest(root, k)
  smallestTest2 = kthSmallest(root1, k1)
  smallestTest3 = kthSmallest(root2, k2)
  smallestTest4 = kthSmallest(root3, k3)
  print("Brute Force -> Test Case 1: ", smallestTest1)
  print("Brute Force -> Test Case 2: ", smallestTest2)
  print("Brute Force -> Test Case 3: ", smallestTest3)
  print("Brute Force -> Test Case 4: ", smallestTest4, "\n")
  
  smallest1Test1 = kthSmallest1(root, k)
  smallest1Test2 = kthSmallest1(root1, k1)
  smallest1Test3 = kthSmallest1(root2, k2)
  smallest1Test4 = kthSmallest1(root3, k3)
  print("In Order Traversal -> Test Case 1: ", smallest1Test1)
  print("In Order Traversal -> Test Case 2: ", smallest1Test2)
  print("In Order Traversal -> Test Case 3: ", smallest1Test3)
  print("In Order Traversal -> Test Case 4: ", smallest1Test4, "\n")
  
  smallest2Test1 = kthSmallest2(root, k)
  smallest2Test2 = kthSmallest2(root1, k1)
  smallest2Test3 = kthSmallest2(root2, k2)
  smallest2Test4 = kthSmallest2(root3, k3)
  print("Recursive Depth First Search -> Test Case 1: ", smallest2Test1)
  print("Recursive Depth First Search -> Test Case 2: ", smallest2Test2)
  print("Recursive Depth First Search -> Test Case 3: ", smallest2Test3)
  print("Recursive Depth First Search -> Test Case 4: ", smallest2Test4, "\n")
  
  smallest3Test1 = kthSmallest3(root, k)
  smallest3Test2 = kthSmallest3(root1, k1)
  smallest3Test3 = kthSmallest3(root2, k2)
  smallest3Test4 = kthSmallest3(root3, k3)
  print("Iterative Depth First Search -> Test Case 1: ", smallest3Test1)
  print("Iterative Depth First Search -> Test Case 2: ", smallest3Test2)
  print("Iterative Depth First Search -> Test Case 3: ", smallest3Test3)
  print("Iterative Depth First Search -> Test Case 4: ", smallest3Test4, "\n")
  
  smallest4Test1 = kthSmallest4(root, k)
  smallest4Test2 = kthSmallest4(root1, k1)
  smallest4Test3 = kthSmallest4(root2, k2)
  smallest4Test4 = kthSmallest4(root3, k3)
  print("Morris Traversal -> Test Case 1: ", smallest4Test1)
  print("Morris Traversal -> Test Case 2: ", smallest4Test2)
  print("Morris Traversal -> Test Case 3: ", smallest4Test3)
  print("Morris Traversal -> Test Case 4: ", smallest4Test4, "\n")