# 695 - Max Area of Island
# Leetcode Link: https://leetcode.com/problems/max-area-of-island/

'''
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:
1 <= grid.length, grid[i].length <= 50
'''

# Solutions To The Problem:
from collections import deque

# Breadth First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def maxAreaOfIsland1(grid):
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  ROWS, COLS = len(grid), len(grid[0])
  area = 0

  def bfs(r, c):
    q = deque()
    grid[r][c] = 0
    q.append((r, c))
    res = 1

    while q:
      row, col = q.popleft()
      for dr, dc in directions:
        nr, nc = dr + row, dc + col
        if (nr < 0 or nc < 0 or nr >= ROWS or
          nc >= COLS or grid[nr][nc] == 0
        ):
          continue
        q.append((nr, nc))
        grid[nr][nc] = 0
        res += 1
    return res

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 1:
        area = max(area, bfs(r, c))

  return area



# Depth First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def maxAreaOfIsland(grid):
  ROWS, COLS = len(grid), len(grid[0])
  visit = set()

  def dfs(r, c):
    if (r < 0 or r == ROWS or c < 0 or
      c == COLS or grid[r][c] == 0 or
      (r, c) in visit
    ):
      return 0
    visit.add((r, c))
    return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

  area = 0
  for r in range(ROWS):
    for c in range(COLS):
      area = max(area, dfs(r, c))
  return area

if __name__ == "__main__":
  grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  ]
  grid1 = [
    [0,0,0,0,0,0,0,0]
  ]
  grid2 = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
  ]
  print("Test Case 1: ", grid)
  print("Expected Output: ", 6)
  print("Test Case 2: ", grid1)
  print("Expected Output: ", 0)
  print("Test Case 3: ", grid2)
  print("Expected Output: ", 6, "\n")
  
  print("Depth First Search -> Test Case 1: ", maxAreaOfIsland(grid))
  print("Depth First Search -> Test Case 2: ", maxAreaOfIsland(grid1))
  print("Depth First Search -> Test Case 3: ", maxAreaOfIsland(grid2), "\n")
  
  print("Breadth First Search -> Test Case 1: ", maxAreaOfIsland1(grid))
  print("Breadth First Search -> Test Case 2: ", maxAreaOfIsland1(grid1))
  print("Breadth First Search -> Test Case 3: ", maxAreaOfIsland1(grid2), "\n")