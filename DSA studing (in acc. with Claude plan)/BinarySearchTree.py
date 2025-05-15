# https://leetcode.com/problems/validate-binary-search-tree/
'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false

Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-2 ** 31 <= Node.val <= 2 ** 31 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#
#         stack = [(root, False)]
#         latest_in_order = []
#
#         while stack:
#             node, visited = stack.pop()
#
#             if visited is True:
#                 if not latest_in_order:
#                     latest_in_order.append(node.val)
#                 else:
#                     latest = latest_in_order.pop()
#                     if latest >= node.val:
#                         return False
#                     else:
#                         latest_in_order.append(node.val)
#                 continue
#
#             if node.right and not visited:
#                 stack.append((node.right, False))
#             stack.append((node, True))
#             if node.left and not visited:
#                 stack.append((node.left, False))
#
#         return True


