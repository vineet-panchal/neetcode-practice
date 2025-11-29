# 128 - Longest Consecutive Sequence
# Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence/

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
Initial Thoughts

Simplify the problem:
  - Given an unsorted array, find length of longest consecutive sequence
  - Must run in O(n) time
  - Return the length as integer

Pattern Recognition: Straightforward solution
  - Sort array, scan for consecutive numbers
  - Track max length, reset on gaps
  - Simple but O(n log n) time

Pattern Recognition: Optimal solution
  - Use set for O(1) lookups
  - For each number, expand sequence only if it's start
  - Achieve O(n) time and O(n) space
  - Efficient for large arrays
'''

# Sets
# Time Complexity: O(n)
# Space Complexity: O(n)
def longestConsecutive(nums):
  s = set(nums)
  ans = 0
  for x in nums:
    if x - 1 not in s:
      y = x + 1
      while y in s:
        y += 1
      ans = max(ans, y - x)
  return ans



# Sets 2
# Time Complexity: O(n)
# Space Complexity: O(n)
def longestConsecutive1(nums):
  # 1. Use a set for O(1) average time complexity lookups
  num_set = set(nums)
  longest_streak = 0
  # 2. Iterate through all unique numbers
  for num in num_set:
    # 3. Check if the current number is the start of a sequence
    # (i.e., num - 1 is not in the set)
    if num - 1 not in num_set:
      current_num = num
      current_streak = 1
      # 4. If it's a start, count the length of the sequence
      while current_num + 1 in num_set:
        current_num += 1
        current_streak += 1
      # 5. Update the global maximum streak
      longest_streak = max(longest_streak, current_streak)
  return longest_streak

if __name__ == "__main__":
  nums = [100, 4, 200, 1, 3, 2]
  nums1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
  print("Sets -> Test Case 1: ", longestConsecutive(nums))
  print("Sets -> Test Case 2: ", longestConsecutive(nums1), "\n")
  print("Sets 2 -> Test Case 1: ", longestConsecutive1(nums))
  print("Sets 2 -> Test Case 2: ", longestConsecutive1(nums1), "\n")