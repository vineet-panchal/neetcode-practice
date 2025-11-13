'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
'''

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


def mergeTwoLists(list1: ListNode, list2: ListNode):
  dummy = node = ListNode()
  
  while list1 and list2:
    if list1.val < list2.val:
      node.next = list1
      list1 = list1.next
    else:
      node.next = list2
      list2 = list2.next
    node = node.next

  node.next = list1 or list2
  return dummy.next

if __name__ == "__main__":
  list11 = build_list([1, 2, 4])
  list12 = build_list([1, 3, 5])
  merged_head = mergeTwoLists(list11, list12)
  print(to_list(merged_head))  # [1, 1, 2, 3, 4, 5]

  list21 = build_list([])
  list22 = build_list([1, 2])
  merged_head2 = mergeTwoLists(list21, list22)
  print(to_list(merged_head2)) # [1, 2]

  list31 = build_list([])
  list32 = build_list([])
  merged_head3 = mergeTwoLists(list31, list32)
  print(to_list(merged_head3)) # []