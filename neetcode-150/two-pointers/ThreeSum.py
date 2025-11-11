'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
'''

def threeSum(nums):
  res = [] # initialize resulting list
  nums.sort() # sort input list nums

  for i, a in enumerate(nums): # loop through the list, with both index (i) and elements (a)
    if i > 0 and a == nums[i - 1]:
      # check if there are duplicate numbers
      # if we already processed this value as the first number, skip it to avoid duplicate triplets
      continue
            
    left = i + 1 # set left pointer to start right after i
    right = len(nums) - 1 # set right pointer as the end of the list

    while left < right: # while left is less than right
      threeSum = a + nums[left] + nums[right] 
      # calculate current three sum by adding a, left element, and right element
      if threeSum > 0: 
      # if the current three sum is less than 0, then it is negative, and we should lower our bigger value
        right -= 1 # decrement the right pointer
      elif threeSum < 0:
      # else if the current three sum is greater than 0, then it is positive, and we should increase our smaller value
        left += 1 # increment left pointer
      else: # else our three sum is equal to 0
        res.append([a, nums[left], nums[right]]) # append that solution to our return list
        left += 1 # increase left pointer
        while nums[left] == nums[left - 1] and left < right:
        # skip duplicate second numbers
        # after finding a valid triplet, skip duplicate values for the second number to avoid duplicate results
          left += 1 
  return res # return our resulting list
# Time Complexity: O(n^2)
# Space Complexity: O(1) without output, O(n) or O(n^2) if we include the output

if __name__ == "__main__":
  print(threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
  print(threeSum([0, 1, 1])) # []