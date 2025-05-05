# https://leetcode.com/problems/linked-list-cycle-ii/description/
'''
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to
(0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
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
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         seen_nodes = set()
#
#         while head:
#             if head in seen_nodes:
#                 return head
#             seen_nodes.add(head)
#             head = head.next
#
#         return None
#
# #Solution2
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         while head:
#             rabbit = head
#             turtle = head
#
#             while rabbit and rabbit.next:
#                 rabbit = rabbit.next.next
#                 turtle = turtle.next
#
#                 if rabbit == turtle:
#                     if rabbit == head:
#                         return head
#                     else:
#                         break
#             else:
#                 return None
#             head = head.next
#
#         return None


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''
19. Remove Nth Node From End of List

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
 

Follow up: Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#
#         current_node = head
#         before_nth_node, nth_node, after_nth_node = None, None, None
#         size = 1
#
#         while current_node:
#             if after_nth_node: after_nth_node = after_nth_node.next
#             if nth_node: nth_node = nth_node.next
#             if before_nth_node: before_nth_node = before_nth_node.next
#
#             if size - n == -1: after_nth_node = head
#             if size - n == 0: nth_node = head
#             if size - n == 1: before_nth_node = head
#
#             size += 1
#             current_node = current_node.next
#
#         if after_nth_node and before_nth_node:
#             before_nth_node.next = after_nth_node
#         elif after_nth_node and not before_nth_node:
#             head = after_nth_node
#         elif before_nth_node and not after_nth_node:
#             before_nth_node.next = None
#         else:
#             head = None
#
#         return head

