# https://leetcode.com/problems/longest-common-prefix/
'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

# Solution1
# from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         common_prefix = ''
#         for letters in zip(*strs):
#             letter = set(letters)
#             if len(letter) == 1:
#                 common_prefix += letters[0]
#             else:
#                 return common_prefix
#         return common_prefix

# testcases
# solution = Solution()
# print(solution.longestCommonPrefix(["flower","flow","flight"]), '-->', 'fl')
# print(solution.longestCommonPrefix(["flower","","flight"]), '-->', '')
# print(solution.longestCommonPrefix(["flower","flower","flower"]), '-->', 'flower')
# print(solution.longestCommonPrefix(["dog","racecar","car"]), '-->', '')


