'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [22,21,20]
Output: [0,0,0]

Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
'''

def dailyTemperatures(temperatures):
  result = [] # initialize resulting list
  left = 0 # set left pointer of the window
    
  while left < len(temperatures): # while the left pointer has not reached end of the list yet
    found = False # intialize found, for whenever we have found a warmer temperature
    for right in range(left + 1, len(temperatures)): 
    # let the right pointer go through the list, starting with the element right after the left pointer
      if temperatures[right] > temperatures[left]:
      # if we have found a warmer temperature
        result.append(right - left) # then find the days till warmer temp and add that to the result
        found = True # set found to true, because we have found a warmer temp
        break # break the loop for right pointer, it doesn't have to look any further
    if not found: # if we haven't found a warmer temperature
      result.append(0) # append 0 to the result
    left += 1 # increment the left pointer, to look at the next day
  return result


def dailyTemperatures1(temperatures):
    result = [0] * len(temperatures) # set the result to be the same size as temperatures
    stack = []  # Stack stores indices
    for i in range(len(temperatures)): # loop through temperatures
        # While stack is not empty AND current temp is warmer than stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop() # get the previous index
            result[prev_index] = i - prev_index # append to the list with the days till warmer day
        stack.append(i) # append index i to the stack, if it is not empty
    return result
# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == "__main__":
  print(dailyTemperatures([30, 38, 30, 36, 35, 40, 28])) # [1, 4, 1, 2, 1, 0, 0]
  print(dailyTemperatures([22, 21, 20])) # [0, 0, 0]
  print(dailyTemperatures1([30, 38, 30, 36, 35, 40, 28])) # [1, 4, 1, 2, 1, 0, 0]
  print(dailyTemperatures1([22, 21, 20])) # [0, 0, 0]