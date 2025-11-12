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