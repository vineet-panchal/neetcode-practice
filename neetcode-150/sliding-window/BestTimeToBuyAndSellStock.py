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

def maxProfit(self, prices) -> int:
  left = 0
  right = 1
  maxPrice = 0

  while right < len(prices):
    if prices[left] < prices[right]:
      profit = prices[right] - prices[left]
      maxPrice = max(maxPrice, profit)
    else:
      left = right
      right += 1
        
  return maxPrice

if __name__ == "__main__":
  prices = [10,1,5,6,7,1]
  print(maxProfit(prices))
  prices = [10,8,7,5,2]
  print(maxProfit(prices))