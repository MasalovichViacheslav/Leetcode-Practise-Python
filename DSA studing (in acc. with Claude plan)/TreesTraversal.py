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


# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
'''
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values. 

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#Solution1
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#
#         if not root:
#             return []
#
#         stack = [root]
#         order = []
#
#         while stack:
#             node = stack.pop()
#             order.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#
#         return order

#Solution2
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#
#         order = []
#
#         def preorder(node):
#             if not node:
#                 return
#             order.append(node.val)
#             preorder(node.left)
#             preorder(node.right)
#
#         preorder(root)
#
#         return order


