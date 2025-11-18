# 200 - Number of Islands
# Leetcode Link: https://leetcode.com/problems/number-of-islands/

'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Constraints:
1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
'''

# Solutions To The Problem:
from collections import deque

# Breadth First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def numIslands1(grid):
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  ROWS, COLS = len(grid), len(grid[0])
  islands = 0

  def bfs(r, c):
    q = deque()
    grid[r][c] = "0"
    q.append((r, c))

    while q:
      row, col = q.popleft()
      for dr, dc in directions:
        nr, nc = dr + row, dc + col
        if (nr < 0 or nc < 0 or nr >= ROWS or
          nc >= COLS or grid[nr][nc] == "0"
        ):
          continue
        q.append((nr, nc))
        grid[nr][nc] = "0"

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "1":
        bfs(r, c)
        islands += 1

  return islands



# Depth First Search
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def numIslands(grid):
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  ROWS, COLS = len(grid), len(grid[0])
  islands = 0

  def dfs(r, c):
    if (r < 0 or c < 0 or r >= ROWS or
      c >= COLS or grid[r][c] == "0"
    ):
      return

    grid[r][c] = "0"
    for dr, dc in directions:
      dfs(r + dr, c + dc)

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "1":
        dfs(r, c)
        islands += 1

  return islands

if __name__ == "__main__":
  grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  grid1 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  print("Test Case 1: grid = ", grid)
  print("Expected Output: ", 1)
  print("Test Case 2: grid = ", grid1)
  print("Expected Output: ", 4, "\n")
  
  print("Depth First Search -> Test Case 1: ", numIslands(grid))
  print("Depth First Search -> Test Case 2: ", numIslands(grid1), "\n")
  
  print("Breadth First Search -> Test Case 1: ", numIslands1(grid))
  print("Breadth First Search -> Test Case 2: ", numIslands1(grid1))