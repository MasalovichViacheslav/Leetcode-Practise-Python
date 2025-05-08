# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2


Constraints:
The number of nodes in the tree is in the range [0, 10**4].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution1
# class Solution:
#     def maxDepth(self, root) -> int:
#         max_depth = 0
#         if not root:
#             return max_depth
#
#         stack = [[root, False, False]]
#         current_depth = 1
#
#         while stack:
#             if stack[-1][1] is False:
#                 stack[-1][1] = True
#                 if stack[-1][0].left:
#                     stack.append([stack[-1][0].left, False, False])
#                     current_depth += 1
#                 else:
#                     max_depth = current_depth if current_depth > max_depth else max_depth
#             else:
#                 if stack[-1][2] is False:
#                     stack[-1][2] = True
#                     if stack[-1][0].right:
#                         stack.append([stack[-1][0].right, False, False])
#                         current_depth += 1
#                     else:
#                         max_depth = current_depth if current_depth > max_depth else max_depth
#                 else:
#                     if stack[-1][1] is True and stack[-1][2] is True:
#                         stack.pop()
#                         current_depth -= 1
#
#         return max_depth
#
# # Solution 2
# class Solution:
#     def maxDepth(self, root) -> int:
#         max_depth = 0
#         if not root:
#             return max_depth
#
#         root.left_not_visited = True
#         root.right_not_visited = True
#         stack = [root]
#         current_depth = 1
#
#         while stack:
#
#             if stack[-1].left_not_visited:
#                 stack[-1].left_not_visited = False
#                 if stack[-1].left:
#                     stack.append(stack[-1].left)
#                     stack[-1].left_not_visited = True
#                     stack[-1].right_not_visited = True
#                     current_depth += 1
#                 else:
#                     max_depth = current_depth if current_depth > max_depth else max_depth
#             else:
#                 if stack[-1].right_not_visited:
#                     stack[-1].right_not_visited = False
#                     if stack[-1].right:
#                         stack.append(stack[-1].right)
#                         stack[-1].left_not_visited = True
#                         stack[-1].right_not_visited = True
#                         current_depth += 1
#                     else:
#                         max_depth = current_depth if current_depth > max_depth else max_depth
#                 else:
#                     if stack[-1].left_not_visited is False and stack[-1].right_not_visited is False:
#                         stack.pop()
#                         current_depth -= 1
#
#         return max_depth
#
# # Solution3
# class Solution:
#     def maxDepth(self, root) -> int:
#         max_depth = 0
#         if not root:
#             return max_depth
#
#         root.left_not_visited = True
#         root.right_not_visited = True
#         stack = [root]
#         current_depth = 1
#
#         while stack:
#
#             top_node = stack[-1]
#
#             if top_node.left_not_visited:
#                 top_node.left_not_visited = False
#                 if top_node.left:
#                     stack.append(top_node.left)
#                     top_node.left.left_not_visited = True
#                     top_node.left.right_not_visited = True
#                     current_depth += 1
#                 else:
#                     max_depth = current_depth if current_depth > max_depth else max_depth
#             else:
#                 if top_node.right_not_visited:
#                     top_node.right_not_visited = False
#                     if top_node.right:
#                         stack.append(top_node.right)
#                         top_node.right.left_not_visited = True
#                         top_node.right.right_not_visited = True
#                         current_depth += 1
#                     else:
#                         max_depth = current_depth if current_depth > max_depth else max_depth
#                 else:
#                     if top_node.left_not_visited is False and top_node.right_not_visited is False:
#                         stack.pop()
#                         current_depth -= 1
#
#         return max_depth
#
# # testcases
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# node1, node2, node3, node4, node5, node6, node7, node8, node9, node10 = (
#     TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5),
#     TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9), TreeNode(10))
#
# node1.left = node2; node1.right = node3
# node2.left = node4; node2.right = node5
# node3.left = node6
# node5.left = node7; node5.right = node8
# node8.left = node9; node8.right = node10
#
# solution = Solution()
# print(solution.maxDepth(node1))


# https://leetcode.com/problems/same-tree/
'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value. 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10 ** 4 <= Node.val <= 10 ** 4
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#
#         stack_p = [p]
#         stack_q = [q]
#
#         while stack_q and stack_p:
#             node_p = stack_p.pop(); node_q = stack_q.pop()
#
#             if node_p.val != node_q.val:
#                 return False
#
#             if node_p.left and node_q.left:
#                 stack_p.append(node_p.left)
#                 stack_q.append(node_q.left)
#             elif not node_p.left and not node_q.left:
#                 pass
#             else:
#                 return False
#
#             if node_p.right and node_q.right:
#                 stack_p.append(node_p.right)
#                 stack_q.append(node_q.right)
#             elif not node_p.right and not node_q.right:
#                 pass
#             else:
#                 return False
#
#         return True


# https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

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
# Solution 1
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#
#         if not root:
#             return []
#
#         result = []
#         left_visited = True; left_not_visited = False
#         stack = [[root, left_not_visited]]
#
#         while stack:
#             node_info = stack.pop()
#
#             if node_info[1] is left_visited:
#                 result.append(node_info[0].val)
#                 continue
#
#             if node_info[0].right:
#                 stack.append([node_info[0].right, left_not_visited])
#
#             stack.append([node_info[0], left_visited])
#
#             if node_info[0].left:
#                 stack.append([node_info[0].left, left_not_visited])
#
#         return result


