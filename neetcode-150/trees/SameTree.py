# 100 - Same Tree
# Leetcode Link: https://leetcode.com/problems/same-tree/

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
def isSameTree2(p: TreeNode, q: TreeNode) -> bool:
  q1 = deque([p])
  q2 = deque([q])

  while q1 and q2:
    for _ in range(len(q1)):
      nodeP = q1.popleft()
      nodeQ = q2.popleft()

      if nodeP is None and nodeQ is None:
        continue
      if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
        return False

      q1.append(nodeP.left)
      q1.append(nodeP.right)
      q2.append(nodeQ.left)
      q2.append(nodeQ.right)

  return True



# Iterative Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isSameTree1(p: TreeNode, q: TreeNode) -> bool:
  stack = [(p, q)]

  while stack:
    node1, node2 = stack.pop()

    if not node1 and not node2:
        continue
    if not node1 or not node2 or node1.val != node2.val:
      return False

    stack.append((node1.right, node2.right))
    stack.append((node1.left, node2.left))

  return True



# Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
  if not p and not q: # if tree p and tree q are empty
    return True # then they are the same
  
  if p and q and p.val == q.val: 
  # if there is a node in tree p and a node in tree q and the value of the nodes are the same
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    # then recursively check if the left and right subtrees are the same
  return False # if they are not return false


if __name__ == "__main__":
  p = build_tree([1, 2, 3])
  q = build_tree([1, 2, 3])
  p1 = build_tree([1, 2])
  q1 = build_tree([1, None, 2])
  p2 = build_tree([1, 2, 1])
  q2 = build_tree([1, 1, 2])
  print("Test Case 1: p = ", [1, 2, 3], ", q = ", [1, 2, 3])
  print("Expected Output: ", True)
  print("Test Case 2: p = ", [1, 2], " q = ", [1, None, 2])
  print("Expected Output: ", False)
  print("Test Case 3: p = ", [1, 2, 1], " q = ", [1, 1, 2])
  print("Expected Output: ", False, "\n")
  
  sameTest1 = isSameTree(p, q)
  sameTest2 = isSameTree(p1, q1)
  sameTest3 = isSameTree(p2, q2)
  print("Depth First Search: ", sameTest1)
  print("Depth First Search: ", sameTest2)
  print("Depth First Search: ", sameTest3)
  
  same1Test1 = isSameTree1(p, q)
  same1Test2 = isSameTree1(p1, q1)
  same1Test3 = isSameTree1(p2, q2)
  print("Depth First Search: ", same1Test1)
  print("Depth First Search: ", same1Test2)
  print("Depth First Search: ", same1Test3)
  
  same2Test1 = isSameTree2(p, q)
  same2Test2 = isSameTree2(p1, q1)
  same2Test3 = isSameTree2(p2, q2)
  print("Depth First Search: ", same2Test1)
  print("Depth First Search: ", same2Test2)
  print("Depth First Search: ", same2Test3)