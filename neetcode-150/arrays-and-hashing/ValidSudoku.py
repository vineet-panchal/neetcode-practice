# 36 - Valid Sudoku
# Leetcode Link: https://leetcode.com/problems/valid-sudoku/

'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
  ["4",".",".","5",".",".",".",".","."],
  [".","9","8",".",".",".",".",".","3"],
  ["5",".",".",".","6",".",".",".","4"],
  [".",".",".","8",".","3",".",".","5"],
  ["7",".",".",".","2",".",".",".","6"],
  [".",".",".",".",".",".","2",".","."],
  [".",".",".","4","1","9",".",".","8"],
  [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
  ["4",".",".","5",".",".",".",".","."],
  [".","9","1",".",".",".",".",".","3"],
  ["5",".",".",".","6",".",".",".","4"],
  [".",".",".","8",".","3",".",".","5"],
  ["7",".",".",".","2",".",".",".","6"],
  [".",".",".",".",".",".","2",".","."],
  [".",".",".","4","1","9",".",".","8"],
  [".",".",".",".","8",".",".","7","9"]]
Output: false
'''

'''
How it works:
Data structures:

rows: tracks which numbers appear in each row (indexed 0-8)
cols: tracks which numbers appear in each column (indexed 0-8)
squares: tracks which numbers appear in each 3x3 box (indexed by position like (0,0), (0,1), etc.)

All three use defaultdict(set) so each key automatically gets an empty set.
The algorithm:

Iterate through every cell (9×9 = 81 cells)
Skip empty cells marked with "."
Check for duplicates: Before adding a number, check if it already exists in:

The current row: rows[row]
The current column: cols[col]
The current 3x3 box: squares[(row // 3, col // 3)]

If found in any of these, return False (invalid)
Record the number: Add it to all three tracking structures
Return True if we complete the loop without finding duplicates

Key insight - the box calculation:
pythonsquares[(row // 3, col // 3)]
This maps any cell to its 3x3 box. For example:

Cell (0,0) to (2,8) → box (0,0) - top-left
Cell (3,3) to (5,5) → box (1,1) - center
Cell (6,6) to (8,8) → box (2,2) - bottom-right

The integer division // groups every 3 rows/columns together, creating 9 unique box identifiers.
Time complexity: O(1) since we always check 81 cells
Space complexity: O(1) since we store at most 81 numbers across our data structures
'''


from collections import defaultdict

def isValidSudoku(board) -> bool:
  cols = defaultdict(set) # create a hashmap for cols, to track numbers in each col
  rows = defaultdict(set) # create a hashmap for rows, to track numbers in each row
  squares = defaultdict(set) # create a hashmap for each 3 * 3 subgrid
  for row in range(9): # go through each row
    for col in range(9): # go through each col
      if board[row][col] == ".": # if a cell is empty
        continue # then skip to the next cell
      # before adding a number into our hashmaps, check if it already exists in row, col, and subgrid
      if (board[row][col] in rows[row] or # does number exist in the row
          board[row][col] in cols[col] or # does number exist in the col
          board[row][col] in squares[(row // 3, col // 3)]): # does number exist in the subgrid
        return False # if found any of these, the board is invalid
      cols[col].add(board[row][col]) # add the number to the set
      rows[row].add(board[row][col]) # add the number to the set
      squares[(row // 3, col // 3)].add(board[row][col])
      # This maps each cell to its 3×3 sub-grid using integer division:
      # Cells at rows 0-2 and cols 0-2 → square (0, 0)
      # Cells at rows 0-2 and cols 3-5 → square (0, 1)
      # Cells at rows 6-8 and cols 6-8 → square (2, 2)
      # So there are 9 possible square keys: (0,0) through (2,2).
  return True

# Time complexity: O(1) since the board is always 9x9
# Space complexity: O(1) since the board is always 9x9


if __name__ == "__main__":
  # Test cases
  board1 = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
  print(isValidSudoku(board1)) # True

  board2 = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",'.','5'],
            ["7",'.',".",'.',"2",'.',".",'.',"6"],
            [".",'.',".",'.',".",'.',"2",'.',"."],
            [".",'.',".",'4',"1",'9',".",'.',"8"],
            [".",'.',".",'.',"8",'.',".",'7',"9"]]
  print(isValidSudoku(board2)) # False
  
  board3 = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",'.',".",'.',"8",'.',".",'7',"9"]]
  print(isValidSudoku(board3)) # True