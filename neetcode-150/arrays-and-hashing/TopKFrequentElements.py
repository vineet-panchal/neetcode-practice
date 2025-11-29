# 347 - Top K Frequent Elements
# Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/

'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
'''

'''
Initial Thoughts

Simplify the problem:
  - we are given a list and an int k, we are to return the k most frequent elements in a list in any order

Pattern Recognition: Straightforward solution
  - we would need a way to count all the frequencies, so we can use a hashmap
  - we could then order the hashmap so the highest frequencies are at the top, then return the k most frequent values
  - however, the time complexity for this approach is O(n log n) because the time complexity mostly comes from the sort function

Pattern Recognition: Optimal solution
  - we should still use a hashmap to get the frequencies, i don't believe there is a better way we can do that
  - we need to basically improve the way we are sorting the hashmap, we can use bucket sort for that
  - 
'''

# Solutions To The Problem:
from collections import Counter

# Counter 
# Time complexity: O(n log n)
# Space complexity: O(n)
def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]



# Counter with sorting
# Time complexity: O(n log n)
# Space complexity: O(n)
def topKFrequent2(nums, k):
    count = Counter(nums)
    return [num for num, freq in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]



# Bucket Sort
# Time complexity: O(n)
# Space complexity: O(n)
def topKFrequent3(nums, k):
    count = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        bucket[freq].append(num)
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        if bucket[i]:
            res.extend(bucket[i])
        if len(res) >= k:
            return res[:k]



# Another Bucket Sort Implementation
# Time complexity: O(n)
# Space complexity: O(n)
def topKFrequent4(nums, k):
  count = {} # intialize hashmap to count elements
  for n in nums: # for each element of nums
    count[n] = 1 + count.get(n, 0) # add 1, if it is already in hashmap, else put it as 0
  
  freq = [[] for i in range(len(nums) + 1)]
  # this creates a list of lists where the index represents frequency
  # the max possible frequency is len(nums), where all the elements are the same
        
  for n, c in count.items(): # group numbers by frequency
    freq[c].append(n) # match the index with the frequency, and put the element their

  res = [] # resulting list to collect top k elements
  for i in range(len(freq) - 1, 0, -1): # loop backwards because the top frequencies are at the end
    for n in freq[i]: # get the element from the index
      res.append(n) # add the element to the result
      if len(res) == k: # when we got the first k elements
        return res # return the resulting list



# Sorting Based on Frequency and Hash Map
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def topKFrequent5(nums, k):
  count = {}
  for n in nums: 
    count[n] = 1 + count.get(n, 0)

  sorted_count = sorted(count, key=count.get, reverse=True)
  return sorted_count[0:k]

if __name__ == "__main__":
  print("Test Case 1: nums = ", [1,2,2,3,3,3], " k = ", 2) # [2,3]
  print("Test Case 2: nums = ", [7,7], " k = ", 1, "\n") # [7]
  
  # Test cases
  print(topKFrequent([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent([7,7], 1)) # [7]
  print(topKFrequent2([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent2([7,7], 1)) # [7]
  print(topKFrequent3([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent3([7,7], 1)) # [7]
  print(topKFrequent4([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent4([7,7], 1)) # [7]