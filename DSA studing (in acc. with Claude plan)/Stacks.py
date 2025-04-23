# https://leetcode.com/problems/backspace-string-compare/
'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
'''
#Solution1
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_backspaced = []
#         for letter in s:
#             if letter.isalpha():
#                 s_backspaced.append(letter)
#             else:
#                 if s_backspaced:
#                     s_backspaced.pop()
#
#         t_backspaced = []
#         for letter in t:
#             if letter.isalpha():
#                 t_backspaced.append(letter)
#             else:
#                 if t_backspaced:
#                     t_backspaced.pop()
#
#         return s_backspaced == t_backspaced

#Solution2
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:


# testcases
# solution = Solution()
# print(solution.backspaceCompare('ab#c', 'ad#c'), 'expected', True)
# print(solution.backspaceCompare('ab##', 'c#d#'), 'expected', True)
# print(solution.backspaceCompare('a#c', 'b'), 'expected', False)
# print(solution.backspaceCompare('###a#c', 'b#c'), 'expected', True)


