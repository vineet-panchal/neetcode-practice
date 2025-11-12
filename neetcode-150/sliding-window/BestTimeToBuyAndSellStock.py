'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
'''

def maxProfit(prices) -> int:
  left = 0 # set left pointer to the start of the list
  right = 1 # set right pointer to the element after left
  maxProfit = 0 # set maxPrice to 0

  while right < len(prices): # while right has not reached the end of the list
    if prices[left] < prices[right]: 
    # if left element is less than the right element, then we have a potential profit
      profit = prices[right] - prices[left] # calculate current profit
      maxProfit = max(maxProfit, profit) 
      # get the max profit which is the max between current profit, and previous max profit
    else: # else, the left element is greater than the right element
      left = right 
      # set the left pointer to right pointer, because we can't even find profit, if right is smaller than left
      right += 1 # increment right by 1, so that it is always 1 greater than left
  return maxProfit # return the max profit

if __name__ == "__main__":
  prices = [10,1,5,6,7,1]
  print(maxProfit(prices))
  prices = [10,8,7,5,2]
  print(maxProfit(prices))