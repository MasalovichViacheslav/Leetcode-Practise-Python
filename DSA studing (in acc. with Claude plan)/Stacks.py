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


# https://leetcode.com/problems/remove-outermost-parentheses/description/
'''
1021. Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, 
and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, 
with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are 
primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

1 <= s.length <= 10 ** 5
s[i] is either '(' or ')'.
s is a valid parentheses string.
'''
# Solution1
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         stack = []
#         result = []
#         primitive = []
#         for bracket in s:
#             if bracket == "(":
#                 stack.append(bracket)
#                 primitive.append(bracket)
#             else:
#                 stack.pop()
#                 primitive.append(bracket)
#
#             if not stack and primitive:
#                 result.append(''.join(primitive[1:len(primitive) - 1]))
#                 primitive.clear()
#
#         return ''.join(result)

# Solution2
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         brackets_count = 0
#         result = ''
#         for bracket in s:
#             if not brackets_count and bracket == "(":
#                 brackets_count += 1
#             elif bracket == "(":
#                 brackets_count += 1
#                 result += bracket
#             elif brackets_count == 1 and bracket == ")":
#                 brackets_count -= 1
#             elif bracket == ")":
#                 brackets_count -= 1
#                 result += bracket
#
#         return result


# testcases
# solution = Solution()
# print(solution.removeOuterParentheses("(()())(())"), 'expected:', '()()()')
# print(solution.removeOuterParentheses("(()())(())(()(()))"), 'expected:', '()()()()(())')
# print(solution.removeOuterParentheses("()()"), 'expected:', '')


