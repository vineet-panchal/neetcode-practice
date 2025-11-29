# 74 - Search A 2D Matrix
# Leetcode Link: https://leetcode.com/problems/search-a-2d-matrix/

'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

def searchMatrix(matrix, target):
  for i in range(len(matrix)):
    left = 0
    right = len(matrix[i]) - 1
    while left <= right:
      mid = int((right + left) / 2)
      if target > matrix[i][mid]:
        left = mid + 1
      elif target < matrix[i][mid]:
        right = mid - 1
      else: 
        return True
  return False

if __name__ == "__main__":
  print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # True