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

from collections import defaultdict
def isValidSudoku(board) -> bool:
  cols = defaultdict(set)
  rows = defaultdict(set)
  squares = defaultdict(set)

  for row in range(9):
    for col in range(9):
      if board[row][col] == ".":
        continue
      if (board[row][col] in rows[row] or
          board[row][col] in cols[col] or
          board[row][col] in squares[(row // 3, col // 3)]):
        return False
      cols[col].add(board[row][col])
      rows[row].add(board[row][col])
      squares[(row // 3, col // 3)].add(board[row][col])
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