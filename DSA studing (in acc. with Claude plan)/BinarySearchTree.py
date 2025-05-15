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


# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
'''
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node 
does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10**7
root is a binary search tree.
1 <= val <= 10**7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution1
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#
#         stack = [(root, False)]
#
#         while stack:
#             node, visited = stack.pop()
#             if visited:
#                 if node.val != val:
#                     continue
#                 else:
#                     return node
#
#             if node.right:
#                 stack.append((node.right, False))
#             stack.append((node, True))
#             if node.left:
#                 stack.append((node.left, False))
#
#         return None
#
# # Solution2
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#
#         subtree = None
#
#         def inorder(node):
#             if not node:
#                 return
#             inorder(node.left)
#             nonlocal subtree
#             if node.val == val:
#                 subtree = node
#                 return
#             inorder(node.right)
#
#         inorder(root)
#
#         return subtree
#
# # Solution3
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#
#         subtree = None
#
#         def inorder(node):
#             nonlocal subtree
#             if not node or subtree:
#                 return
#             inorder(node.left)
#             if node.val == val:
#                 subtree = node
#                 return
#             inorder(node.right)
#
#         inorder(root)
#
#         return subtree
#
#
# # Solution4
# from collections import deque
#
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#
#         nodes = deque()
#         nodes.append(root)
#
#         while nodes:
#             node = nodes.popleft()
#             if node.val == val:
#                 return node
#
#             if node.right:
#                 nodes.append(node.right)
#             if node.left:
#                 nodes.append(node.left)
#
#         return None
#
# # Solution5
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         node = root
#         while True:
#             if node.val == val:
#                 return node
#             elif val < node.val and node.left:
#                 node = node.left
#             elif val > node.val and node.right:
#                 node = node.right
#             else:
#                 return None

