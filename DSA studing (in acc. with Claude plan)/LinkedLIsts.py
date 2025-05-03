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


