# https://leetcode.com/problems/reverse-linked-list/
'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# # Solution1
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head):
#
#         if not head:
#             return head
#
#         previous_node = None
#
#         while head.next is not None:
#             new_head = head
#             head = head.next
#             new_head.next = previous_node
#             previous_node = new_head
#         new_head = head
#         new_head.next = previous_node
#
#         return new_head


# https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#
#         if not list1:
#             return list2
#         elif not list2:
#             return list1
#
#         merged = None
#
#         while list1 and list2:
#
#             if not merged:
#                 if list1.val <= list2.val:
#                     merged = list1
#                     list1 = list1.next
#                 else:
#                     merged = list2
#                     list2 = list2.next
#                 new_header = merged
#             else:
#                 if list1.val <= list2.val:
#                     merged.next = list1
#                     list1 = list1.next
#                 else:
#                     merged.next = list2
#                     list2 = list2.next
#                 merged = merged.next
#
#         if list1:
#             merged.next = list1
#         else:
#             merged.next = list2
#
#         return new_header


# https://leetcode.com/problems/linked-list-cycle/description/
'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
The number of the nodes in the list is in the range [0, 10 ** 4].
-10 ** 5 <= Node.val <= 10 ** 5
pos is -1 or a valid index in the linked-list. 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # Solution1
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#
#         nodes = {head}
#         nodes_length = 1
#         while head:
#             nodes.update({head.next})
#             if nodes_length == len(nodes):
#                 return True
#             head = head.next
#             nodes_length += 1
#         return False
#
# #Solution2
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#
#         nodes = {head}
#         while head:
#             if head.next in nodes:
#                 return True
#             nodes.add(head.next)
#             head = head.next
#         return False


