# 133 - Clone Graph
# Leetcode Link: https://leetcode.com/problems/clone-graph/

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def buildGraph(adjList):
  if not adjList:
    return None
  nodes = [Node(i+1) for i in range(len(adjList))]
  for i, neighbors in enumerate(adjList):
    for nei in neighbors:
      nodes[i].neighbors.append(nodes[nei-1])
  return nodes[0]

def getAdjList(node):
  if not node:
    return []
  visited = set()
  nodes = []
  q = deque([node])
  visited.add(node)
  while q:
    cur = q.popleft()
    nodes.append(cur)
    for nei in cur.neighbors:
      if nei not in visited:
        visited.add(nei)
        q.append(nei)
  nodes.sort(key=lambda x: x.val)
  return [[nei.val for nei in n.neighbors] for n in nodes]

'''
Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: The graph is empty.

Constraints:
0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
'''

# Solutions To The Problem
from collections import deque
from typing import Optional

# Breadth First Search
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def cloneGraphBFS(node: Optional['Node']) -> Optional['Node']:
  if not node:
    return None

  oldToNew = {}
  oldToNew[node] = Node(node.val)
  q = deque([node])

  while q:
    cur = q.popleft()
    for nei in cur.neighbors:
      if nei not in oldToNew:
        oldToNew[nei] = Node(nei.val)
        q.append(nei)
      oldToNew[cur].neighbors.append(oldToNew[nei])

  return oldToNew[node]

# Depth First Search
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def cloneGraphDFS(node: Optional['Node']) -> Optional['Node']:
  oldToNew = {}
  def dfs(node):
    if node in oldToNew:
      return oldToNew[node]
    copy = Node(node.val)
    oldToNew[node] = copy
    for nei in node.neighbors:
      copy.neighbors.append(dfs(nei))
    return copy
  return dfs(node) if node else None

if __name__ == "__main__":
  # Test cases
  test_cases = [
    ([[2],[1,3],[2]], [[2],[1,3],[2]]),
    ([[]], [[]]),
    ([], [])
  ]

  for i, (input_adj, expected) in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print(f"Input: {input_adj}")
    print(f"Expected: {expected}")

    # Build graph from adjList
    node = buildGraph(input_adj)

    # Test BFS
    cloned_bfs = cloneGraphBFS(node)
    result_bfs = getAdjList(cloned_bfs)
    print(f"BFS Result: {result_bfs}")
    print(f"BFS Passed: {result_bfs == expected}")

    # Test DFS
    cloned_dfs = cloneGraphDFS(node)
    result_dfs = getAdjList(cloned_dfs)
    print(f"DFS Result: {result_dfs}")
    print(f"DFS Passed: {result_dfs == expected}")
    print()
  