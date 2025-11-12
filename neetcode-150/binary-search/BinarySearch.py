def binarySearch(nums, target):
  left = 0 # set left pointer for window
  right = len(nums) - 1 # set right pointer to the end of the window
  
  while left <= right: # while left and right don't go over each other
    mid = int(left + (right - left) / 2) 
    # calculate mid with right - left / 2 + left
    if target > nums[mid]: # if target is greater than element at mid
      left = mid + 1 # then target is on right of mid, move left to after mid
    elif target < nums[mid]: # if target is less than element at mid
      right = mid - 1 # then target is on the left of mid, move right to before mid
    else: # else target = element at mid
      return mid # return mid index
  return -1 # else return -1, if we could find it

if __name__ == "__main__":
  print(binarySearch([-1, 0, 2, 4, 6, 8], 4))