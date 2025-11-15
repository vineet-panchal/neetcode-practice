# 226 - Invert Binary Tree
# Leetcode Link: https://leetcode.com/problems/invert-binary-tree/

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
def invertTree1(root: TreeNode) -> TreeNode:
  if not root: # if tree is empty
    return None # then return None, nothing to invert
  queue = deque([root]) # initialize a queue for the tree
  while queue: # while there are still nodes
    node = queue.popleft() # get the first node in the queue
    node.left, node.right = node.right, node.left # swap right and left nodes
    if node.left: # if there is a left node
      queue.append(node.left) # then add it to the queue
    if node.right: # if there is a right node
      queue.append(node.right) # then add it to the queue
  return root # return the inverted queue

'''
Let's trace through a simple tree:
    4
   / \
  2   7
 / \
1   3
Execution:

queue = deque([4])
Popleft 4, swap its children → now 4's left is 7, right is 2
Add 7 and 2 to queue: queue = [7, 2]
Popleft 7, it has no children, nothing to add: queue = [2]
Popleft 2, swap its children → now 2's left is 3, right is 1
Add 3 and 1 to queue: queue = [3, 1]
Popleft 3, it has no children, nothing to add: queue = [1]
Popleft 1, it has no children, nothing to add: queue = []
Queue is empty, done!

Result:
    4
   / \
  7   2
     / \
    3   1
'''



# Depth First Search Recursive Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def invertTree2(root: TreeNode) -> TreeNode:
  if not root: return None # if there is no tree, return None, nothnig to invert
  root.left, root.right = root.right, root.left 
  # swap left and right nodes of current root element

  invertTree(root.left) # recursively call the left node
  invertTree(root.right) # recursively call the right node

  return root # return the inverted root

'''
Let's trace through a simple tree:
    4
   / \
  2   7
 / \
1   3

Execution (Call Stack):
1. invertTree(4) called
  - Swap 4's children → now 4's left is 7, right is 2
  - Call invertTree(7) (left child)
2. invertTree(7) called
  - 7 has no children (both None)
  - Swap does nothing: None, None = None, None
  - Call invertTree(None) (left) → returns None immediately
  - Call invertTree(None) (right) → returns None immediately
  - Return 7
3. Back to invertTree(4), now call invertTree(2) (right child)
4. invertTree(2) called
  - Swap 2's children → now 2's left is 3, right is 1
  - Call invertTree(3) (left child)
5. invertTree(3) called
  - 3 has no children
  - Swap does nothing
  - Calls return None immediately
  - Return 3
6. Back to invertTree(2), now call invertTree(1) (right child)
7. invertTree(1) called
  - 1 has no children
  - Swap does nothing
  - Calls return None immediately
  - Return 1
8. Back to invertTree(2), return 2
9. Back to invertTree(4), return 4

Result:
    4
   / \
  7   2
     / \
    3   1
'''



# Depth First Search Iterative Stack Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def invertTree(root: TreeNode) -> TreeNode:
  if not root: # if the tree is empty
    return None # then return None, nothing to invert
  
  stack = [root] # create a stack with the root node
  while stack: # continue while there are still nodes to process
    node = stack.pop() # get the last node, very end right

    temp = node.left
    node.left = node.right
    node.right = temp
    # swap the left and right nodes
    # node.left, node.right = node.right, node.left # alternative swap method

    # add children to the stack
    if node.left: # if node has a left child
      stack.append(node.left) # then add it to the stack
    if node.right: # if node has a right child
      stack.append(node.right) # then add it to the stack
  return root # return the inverted tree

'''
Let's trace through a simple tree:
    4
   / \
  2   7
 / \
1   3

**Execution:**
1. `stack = [4]`
2. Pop `4`, swap its children → now `4`'s left is `7`, right is `2`
3. Add `7` and `2` to stack: `stack = [7, 2]`
4. Pop `2`, swap its children → now `2`'s left is `3`, right is `1`
5. Add `3` and `1` to stack: `stack = [7, 3, 1]`
6. Pop `1`, it has no children, nothing to add
7. Pop `3`, it has no children, nothing to add
8. Pop `7`, it has no children, nothing to add
9. Stack is empty, done!

**Result:**
    4
   / \
  7   2
     / \
    3   1
'''

if __name__ == "__main__":
  root = build_tree([4, 2, 7, 1, 3, 6, 9])
  root2 = build_tree([2,1,3])
  root3 = build_tree([])
  
  print("Test Case 1: ", level_order_traversal(root))
  print("Expected Output: ", [4,7,2,9,6,3,1])
  print("Test Case 2: ", level_order_traversal(root2))
  print("Expected Output: ", [2,3,1])
  print("Test Case 3: ", level_order_traversal(root3))
  print("Expected Output: ", [], "\n")
  
  invertedroot = invertTree(root)
  invertedroot2 = invertTree(root2)
  invertedroot3 = invertTree(root3)
  print("Depth First Search Stack -> Test Case 1: ", level_order_traversal(invertedroot))
  print("Depth First Search Stack -> Test Case 2: ", level_order_traversal(invertedroot2))
  print("Depth First Search Stack -> Test Case 3: ", level_order_traversal(invertedroot3), "\n")
  
  inverted1root = invertTree1(root)
  inverted1root2 = invertTree1(root2)
  inverted1root3 = invertTree1(root3)
  print("Breadth First Search -> Test Case 1: ", level_order_traversal(inverted1root))
  print("Breadth First Search -> Test Case 2: ", level_order_traversal(inverted1root2))
  print("Breadth First Search -> Test Case 3: ", level_order_traversal(inverted1root3), "\n")
  
  inverted2root = invertTree2(root)
  inverted2root2 = invertTree2(root2)
  inverted2root3 = invertTree2(root3)
  print("Depth First Search Recursive -> Test Case 1: ", level_order_traversal(inverted2root))
  print("Depth First Search Recursive -> Test Case 2: ", level_order_traversal(inverted2root2))
  print("Depth First Search Recursive -> Test Case 3: ", level_order_traversal(inverted2root3), "\n")