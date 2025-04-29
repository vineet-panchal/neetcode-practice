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

from collections import Counter
# solution 1
def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]
# Time complexity: O(n log n)
# Space complexity: O(n)

# solution 2
def topKFrequent2(nums, k):
    count = Counter(nums)
    return [num for num, freq in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]
# Time complexity: O(n log n)
# Space complexity: O(n)

# solution 3
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
# Time complexity: O(n)
# Space complexity: O(n)

# solution 4
def topKFrequent4(nums, k):
  count = {}
  freq = [[] for i in range(len(nums) + 1)]

  for n in nums:
    count[n] = 1 + count.get(n, 0)
        
  for n, c in count.items():
    freq[c].append(n)

  res = []
  for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
      res.append(n)
      if len(res) == k:
        return res
# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
  # Test cases
  print(topKFrequent([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent([7,7], 1)) # [7]
  print(topKFrequent2([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent2([7,7], 1)) # [7]
  print(topKFrequent3([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent3([7,7], 1)) # [7]
  print(topKFrequent4([1,2,2,3,3,3], 2)) # [2,3]
  print(topKFrequent4([7,7], 1)) # [7]