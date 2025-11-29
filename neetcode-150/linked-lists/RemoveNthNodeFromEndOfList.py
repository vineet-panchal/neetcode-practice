# 19 - Remove Nth Node From End Of List
# Leetcode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  nodes = []
  cur = head
  while cur:
    nodes.append(cur)
    cur = cur.next

  removeIndex = len(nodes) - n
  if removeIndex == 0:
    return head.next

  nodes[removeIndex - 1].next = nodes[removeIndex].next
  return head



# Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def rec(self, head, n):
    if not head:
        return None

    head.next = self.rec(head.next, n)
    n[0] -= 1
    if n[0] == 0:
        return head.next
    return head

def removeNthFromEnd(self, head, n):
    return self.rec(head, [n])



# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  dummy = ListNode(0, head)
  left = dummy
  right = head

  while n > 0:
    right = right.next
    n -= 1

  while right:
    left = left.next
    right = right.next

  left.next = left.next.next
  return dummy.next