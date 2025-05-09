# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''
102. Binary Tree Level Order Traversal

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#
#         result = []
#         if not root: return result
#
#         stack = [[root]]
#         while stack:
#             add_to_result = []
#             next_level_nodes = []
#
#             for node in stack.pop():
#                 add_to_result.append(node.val)
#                 if node.left:
#                     next_level_nodes.append(node.left)
#                 if node.right:
#                     next_level_nodes.append(node.right)
#
#             result.append(add_to_result)
#             if next_level_nodes:
#                 stack.append(next_level_nodes)
#
#         return result


